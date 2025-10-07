#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sign Language Detection Application

Author: Nayana Pabasara
Created: 2024
Description: Modern GUI application for sign language detection with custom styling
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import cv2
import mediapipe as mp
import numpy as np
import pickle
import threading
import os
from PIL import Image, ImageTk
import subprocess
import sys

class SignLanguageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Language Detector - By Nayana Pabasara")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2c3e50')
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()
        
        # Variables
        self.cap = None
        self.is_detecting = False
        self.model = None
        # Create labels dictionary for A-Z (26 letters) + 0-9 (10 numbers) = 36 total
        self.labels_dict = {}
        # Add letters A-Z (classes 0-25)
        for i in range(26):
            self.labels_dict[i] = chr(ord('A') + i)
        # Add numbers 0-9 (classes 26-35)
        for i in range(10):
            self.labels_dict[i + 26] = str(i)
        
        # MediaPipe setup
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.hands = self.mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.3, min_tracking_confidence=0.3)
        # Custom drawing specs for sharper and thicker landmark lines
        self.landmark_spec = self.mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3)
        self.connection_spec = self.mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=1)
        
        self.setup_ui()
        self.load_model()
        
    def configure_styles(self):
        """Configure custom styles for the application"""
        self.style.configure('Title.TLabel', 
                           font=('Arial', 24, 'bold'),
                           foreground='#ecf0f1',
                           background='#2c3e50')
        
        self.style.configure('Header.TLabel',
                           font=('Arial', 14, 'bold'),
                           foreground='#3498db',
                           background='#2c3e50')
        
        self.style.configure('Info.TLabel',
                           font=('Arial', 10),
                           foreground='#bdc3c7',
                           background='#2c3e50')
        
        self.style.configure('Custom.TButton',
                           font=('Arial', 12, 'bold'),
                           padding=(20, 10))
        
        self.style.map('Custom.TButton',
                      background=[('active', '#3498db'),
                                ('pressed', '#2980b9')])
    
    def setup_ui(self):
        """Setup the user interface"""
        # Main container
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = ttk.Label(main_frame, text="Sign Language Detector", style='Title.TLabel')
        title_label.pack(pady=(0, 20))
        
        # Author label
        author_label = ttk.Label(main_frame, text="Developed by Nayana Pabasara", style='Info.TLabel')
        author_label.pack(pady=(0, 30))
        
        # Control panel
        control_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RAISED, bd=2)
        control_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Control buttons
        button_frame = tk.Frame(control_frame, bg='#34495e')
        button_frame.pack(pady=20)
        
        self.start_btn = ttk.Button(button_frame, text="Start Detection", 
                                  command=self.start_detection, style='Custom.TButton')
        self.start_btn.pack(side=tk.LEFT, padx=10)
        
        self.stop_btn = ttk.Button(button_frame, text="Stop Detection", 
                                 command=self.stop_detection, style='Custom.TButton', state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=10)
        
        self.collect_btn = ttk.Button(button_frame, text="Collect Data", 
                                    command=self.open_data_collection, style='Custom.TButton')
        self.collect_btn.pack(side=tk.LEFT, padx=10)
        
        self.train_btn = ttk.Button(button_frame, text="Train Model", 
                                  command=self.train_model, style='Custom.TButton')
        self.train_btn.pack(side=tk.LEFT, padx=10)
        
        # Status frame
        status_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RAISED, bd=2)
        status_frame.pack(fill=tk.X, pady=(0, 20))
        
        status_label = ttk.Label(status_frame, text="Status", style='Header.TLabel')
        status_label.pack(pady=(10, 5))
        
        self.status_text = tk.Text(status_frame, height=4, bg='#2c3e50', fg='#ecf0f1',
                                 font=('Consolas', 10), wrap=tk.WORD)
        self.status_text.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        # Video frame
        video_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RAISED, bd=2)
        video_frame.pack(fill=tk.BOTH, expand=True)
        
        video_label = ttk.Label(video_frame, text="Camera Feed", style='Header.TLabel')
        video_label.pack(pady=(10, 5))
        
        self.video_label = tk.Label(video_frame, bg='#2c3e50', text="Camera not started")
        self.video_label.pack(pady=(0, 10), padx=10)
        
        # Detection result frame
        result_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RAISED, bd=2)
        result_frame.pack(fill=tk.X, pady=(20, 0))
        
        result_label = ttk.Label(result_frame, text="Detection Result", style='Header.TLabel')
        result_label.pack(pady=(10, 5))
        
        self.result_text = tk.Text(result_frame, height=2, bg='#2c3e50', fg='#e74c3c',
                                 font=('Arial', 16, 'bold'), wrap=tk.WORD)
        self.result_text.pack(fill=tk.X, padx=10, pady=(0, 10))
        
    def log_status(self, message):
        """Log status messages"""
        self.status_text.insert(tk.END, f"{message}\n")
        self.status_text.see(tk.END)
        self.root.update()
        
    def load_model(self):
        """Load the trained model"""
        try:
            if os.path.exists('model.p'):
                model_dict = pickle.load(open('model.p', 'rb'))
                self.model = model_dict['model']
                self.log_status("✓ Model loaded successfully")
            else:
                self.log_status("⚠ No trained model found. Please train a model first.")
        except Exception as e:
            self.log_status(f"✗ Error loading model: {str(e)}")
            
    def start_detection(self):
        """Start real-time detection"""
        if self.model is None:
            messagebox.showerror("Error", "No trained model found. Please train a model first.")
            return
            
        try:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                messagebox.showerror("Error", "Could not open camera")
                return
                
            self.is_detecting = True
            self.start_btn.config(state=tk.DISABLED)
            self.stop_btn.config(state=tk.NORMAL)
            
            self.log_status("✓ Detection started")
            self.detection_thread = threading.Thread(target=self.detection_loop)
            self.detection_thread.daemon = True
            self.detection_thread.start()
            
        except Exception as e:
            self.log_status(f"✗ Error starting detection: {str(e)}")
            
    def stop_detection(self):
        """Stop real-time detection"""
        self.is_detecting = False
        if self.cap:
            self.cap.release()
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.video_label.config(image='', text="Camera stopped")
        self.log_status("✓ Detection stopped")
        
    def detection_loop(self):
        """Main detection loop"""
        while self.is_detecting:
            try:
                ret, frame = self.cap.read()
                if not ret:
                    break
                    
                # Flip frame horizontally
                frame = cv2.flip(frame, 1)
                H, W, _ = frame.shape
                
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = self.hands.process(frame_rgb)
                
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        self.mp_drawing.draw_landmarks(
                            frame,
                            hand_landmarks,
                            self.mp_hands.HAND_CONNECTIONS,
                            self.landmark_spec,
                            self.connection_spec
                        )
                    
                    # Extract features and predict
                    data_aux = []
                    x_ = []
                    y_ = []
                    
                    for hand_landmarks in results.multi_hand_landmarks:
                        for i in range(len(hand_landmarks.landmark)):
                            x = hand_landmarks.landmark[i].x
                            y = hand_landmarks.landmark[i].y
                            x_.append(x)
                            y_.append(y)
                        
                        for i in range(len(hand_landmarks.landmark)):
                            x = hand_landmarks.landmark[i].x
                            y = hand_landmarks.landmark[i].y
                            data_aux.append(x - min(x_))
                            data_aux.append(y - min(y_))
                    
                    # Draw bounding box and prediction
                    x1 = int(min(x_) * W) - 10
                    y1 = int(min(y_) * H) - 10
                    x2 = int(max(x_) * W) + 10
                    y2 = int(max(y_) * H) + 10
                    
                    prediction = self.model.predict([np.asarray(data_aux)])
                    predicted_character = self.labels_dict[int(prediction[0])]
                    
                    # Thicker anti-aliased bounding box for sharper edges
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 8, cv2.LINE_AA)
                    # Larger, bolder detection text with a contrasting background for readability
                    text = predicted_character
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    font_scale = 2.0
                    text_thickness = 5
                    (text_w, text_h), _ = cv2.getTextSize(text, font, font_scale, text_thickness)
                    text_x = x1
                    text_y = max(0, y1 - 12)
                    # Background rectangle behind text (filled)
                    bg_top_left = (text_x - 6, max(0, text_y - text_h - 10))
                    bg_bottom_right = (text_x + text_w + 6, text_y + 6)
                    cv2.rectangle(frame, bg_top_left, bg_bottom_right, (0, 255, 0), -1, cv2.LINE_AA)
                    cv2.putText(frame, text, (text_x, text_y), font, font_scale, (0, 0, 0), text_thickness, cv2.LINE_AA)
                    
                    # Update result display
                    self.result_text.delete(1.0, tk.END)
                    self.result_text.insert(tk.END, f"Detected: {predicted_character}")
                
                # Convert frame for display
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (640, 480))
                image = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image=image)
                
                self.video_label.config(image=photo)
                self.video_label.image = photo
                
            except Exception as e:
                self.log_status(f"✗ Detection error: {str(e)}")
                break
                
    def open_data_collection(self):
        """Open data collection script with interactive menu"""
        try:
            subprocess.Popen([sys.executable, 'collect_imgs.py'])
            self.log_status("✓ Data collection menu opened - Choose Letters, Numbers, or All")
        except Exception as e:
            self.log_status(f"✗ Error opening data collection: {str(e)}")
            
    def train_model(self):
        """Train the model"""
        def train():
            try:
                self.log_status("Starting model training...")
                
                # Create dataset
                subprocess.run([sys.executable, 'create_dataset.py'], check=True)
                self.log_status("✓ Dataset created")
                
                # Train model
                subprocess.run([sys.executable, 'train_classifier.py'], check=True)
                self.log_status("✓ Model training completed")
                
                # Reload model
                self.load_model()
                
            except Exception as e:
                self.log_status(f"✗ Training error: {str(e)}")
                
        threading.Thread(target=train, daemon=True).start()

def main():
    root = tk.Tk()
    app = SignLanguageApp(root)
    
    # Handle window closing
    def on_closing():
        if app.is_detecting:
            app.stop_detection()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
