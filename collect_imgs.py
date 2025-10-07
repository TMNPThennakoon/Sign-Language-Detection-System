#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sign Language Data Collection Module

Author: Nayana Pabasara
Created: 2025
Description: Collects training images for sign language detection with interactive menu
"""

import os
import cv2
import time
import tkinter as tk
from tkinter import ttk, messagebox


# Configuration
DATA_DIR = './data'
dataset_size = 40  # Images per class

# Global variables to store the selected collection mode and specific letter
selected_collection_mode = None
selected_letter = None

def show_collection_options():
    """Displays a Tkinter window for the user to select collection mode."""
    global selected_collection_mode, selected_letter

    root = tk.Tk()
    root.title("Sign Language Data Collection - By Nayana Pabasara")
    root.geometry("600x500")
    root.resizable(False, False)
    root.configure(bg='#2c3e50')  # Dark background

    # Configure style
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TFrame', background='#2c3e50')
    style.configure('TButton', 
                   font=('Arial', 12, 'bold'), 
                   foreground='#ffffff', 
                   background='#34495e',
                   padding=(20, 15), 
                   borderwidth=0, 
                   focusthickness=3, 
                   focuscolor='none')
    style.map('TButton', background=[('active', '#3498db')])  # Blue on hover
    
    # Configure entry style
    style.configure('Custom.TEntry', 
                   font=('Arial', 14, 'bold'),
                   fieldbackground='#34495e',
                   foreground='#ecf0f1',
                   borderwidth=2,
                   relief='solid')

    # Main frame
    frame = ttk.Frame(root, padding="30")
    frame.pack(expand=True, fill='both')

    # Title
    title_label = ttk.Label(frame, 
                           text="Sign Language Data Collection", 
                           font=('Arial', 18, 'bold'),
                           foreground='#ecf0f1', 
                           background='#2c3e50')
    title_label.pack(pady=(0, 10))

    # Subtitle
    subtitle_label = ttk.Label(frame, 
                              text="Choose what to collect:", 
                              font=('Arial', 14),
                              foreground='#bdc3c7', 
                              background='#2c3e50')
    subtitle_label.pack(pady=(0, 20))

    # Letter input section
    letter_frame = ttk.Frame(frame)
    letter_frame.pack(pady=10, fill='x')
    
    letter_label = ttk.Label(letter_frame, 
                           text="🎯 Collect Specific Letter/Number:", 
                           font=('Arial', 12, 'bold'),
                           foreground='#3498db', 
                           background='#2c3e50')
    letter_label.pack(anchor='w')
    
    input_frame = ttk.Frame(letter_frame)
    input_frame.pack(fill='x', pady=(5, 0))
    
    letter_entry = ttk.Entry(input_frame, 
                            style='Custom.TEntry',
                            width=3,
                            justify='center')
    letter_entry.pack(side='left', padx=(0, 10))
    
    def collect_specific_letter():
        global selected_collection_mode, selected_letter
        letter = letter_entry.get().strip().upper()
        
        if not letter:
            messagebox.showerror("Error", "Please enter a letter or number!")
            return
            
        if len(letter) != 1:
            messagebox.showerror("Error", "Please enter only one character!")
            return
            
        if letter.isalpha() and letter.isupper():
            selected_collection_mode = 'specific_letter'
            selected_letter = letter
            root.destroy()
        elif letter.isdigit():
            selected_collection_mode = 'specific_number'
            selected_letter = letter
            root.destroy()
        else:
            messagebox.showerror("Error", "Please enter a valid letter (A-Z) or number (0-9)!")
    
    btn_specific = ttk.Button(input_frame, 
                            text="Collect This Letter/Number", 
                            command=collect_specific_letter)
    btn_specific.pack(side='left')
    
    # Info for specific letter
    info_specific = ttk.Label(letter_frame, 
                            text="Enter A-Z or 0-9 to collect data for that specific symbol", 
                            font=('Arial', 9, 'italic'),
                            foreground='#95a5a6', 
                            background='#2c3e50')
    info_specific.pack(anchor='w', pady=(5, 0))

    # Separator
    separator = ttk.Separator(frame, orient='horizontal')
    separator.pack(fill='x', pady=20)

    # Batch collection options
    batch_label = ttk.Label(frame, 
                           text="📚 Batch Collection Options:", 
                           font=('Arial', 12, 'bold'),
                           foreground='#3498db', 
                           background='#2c3e50')
    batch_label.pack(anchor='w', pady=(0, 10))

    def set_mode_and_destroy(mode):
        global selected_collection_mode
        selected_collection_mode = mode
        root.destroy()

    # Buttons for batch collection
    btn_letters = ttk.Button(frame, 
                            text="📝 Collect All Letters (A-Z)\n26 letters, ~50 minutes", 
                            command=lambda: set_mode_and_destroy('letters'))
    btn_letters.pack(pady=5, fill='x')

    btn_numbers = ttk.Button(frame, 
                            text="🔢 Collect All Numbers (0-9)\n10 numbers, ~20 minutes", 
                            command=lambda: set_mode_and_destroy('numbers'))
    btn_numbers.pack(pady=5, fill='x')

    btn_all = ttk.Button(frame, 
                        text="🔤 Collect All (A-Z + 0-9)\n36 symbols, ~2 hours", 
                        command=lambda: set_mode_and_destroy('all'))
    btn_all.pack(pady=5, fill='x')

    # Info label
    info_label = ttk.Label(frame, 
                          text="💡 Tip: Use specific letter collection to update individual datasets", 
                          font=('Arial', 10, 'italic'),
                          foreground='#95a5a6', 
                          background='#2c3e50')
    info_label.pack(pady=(20, 0))

    root.mainloop()

def main():
    """Main data collection function"""
    global selected_collection_mode, selected_letter
    
    # Show selection menu
    show_collection_options()

    if selected_collection_mode is None:
        print("No collection mode selected. Exiting.")
        return

    # Determine the range of classes based on selection
    if selected_collection_mode == 'letters':
        start_class = 0
        end_class = 26  # A-Z
        print("Selected: Collecting data for Letters (A-Z)")
    elif selected_collection_mode == 'numbers':
        start_class = 26
        end_class = 36  # 0-9
        print("Selected: Collecting data for Numbers (0-9)")
    elif selected_collection_mode == 'all':
        start_class = 0
        end_class = 36  # A-Z and 0-9
        print("Selected: Collecting data for All (A-Z, 0-9)")
    elif selected_collection_mode == 'specific_letter':
        # Convert letter to class number (A=0, B=1, ..., Z=25)
        start_class = ord(selected_letter) - ord('A')
        end_class = start_class + 1
        print(f"Selected: Collecting data for letter '{selected_letter}' (class {start_class})")
    elif selected_collection_mode == 'specific_number':
        # Convert number to class number (0=26, 1=27, ..., 9=35)
        start_class = int(selected_letter) + 26
        end_class = start_class + 1
        print(f"Selected: Collecting data for number '{selected_letter}' (class {start_class})")

    # Create directories for each class if they don't exist
    for i in range(start_class, end_class):
        class_dir = os.path.join(DATA_DIR, str(i))
        if not os.path.exists(class_dir):
            os.makedirs(class_dir)

    # Initialize camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video stream. Check camera connection.")
        return

    print(f"\nStarting data collection for {end_class - start_class} classes...")
    print("Press 'Q' when ready to start collecting for each symbol")
    print("Press 'ESC' to exit at any time\n")

    for j in range(start_class, end_class):
        # Convert class number to letter or number
        if j < 26:
            symbol = chr(ord('A') + j)  # A-Z (0-25)
            symbol_type = "Letter"
        else:
            symbol = str(j - 26)  # 0-9 (26-35)
            symbol_type = "Number"
        
        if selected_collection_mode in ['specific_letter', 'specific_number']:
            print(f'🎯 Collecting data for {symbol_type} "{symbol}" (class {j}) - Specific Collection Mode')
        else:
            print(f'Collecting data for {symbol_type} "{symbol}" (class {j})')

        # Wait for 'Q' key press to start collection for the current class
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame.")
                break

            # Display instruction
            cv2.putText(frame, f'{symbol_type} "{symbol}" - Ready? Press "Q" ! :)', (50, 50), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, f'Class {j+1}/{end_class - start_class}', (50, 100), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
            
            cv2.imshow('frame', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == 27:  # ESC key
                print("Collection cancelled by user.")
                cap.release()
                cv2.destroyAllWindows()
                return

        # Collect images
        counter = 0
        while counter < dataset_size:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame.")
                break

            # Save image with timestamp
            img_path = os.path.join(DATA_DIR, str(j), f'{counter}.jpg')
            cv2.imwrite(img_path, frame)

            # Display progress
            remaining = dataset_size - counter
            cv2.putText(frame, f'Collecting {symbol_type} "{symbol}"', (50, 50), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, f'Progress: {counter+1}/{dataset_size} ({remaining} left)', (50, 100), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2, cv2.LINE_AA)
            
            cv2.imshow('frame', frame)
            cv2.waitKey(2)  # Small delay

            counter += 1

        print(f'✅ Done collecting for {symbol_type} "{symbol}" (class {j})')

    cap.release()
    cv2.destroyAllWindows()
    
    if selected_collection_mode in ['specific_letter', 'specific_number']:
        print(f"\n🎉 Specific data collection complete! Updated dataset for '{selected_letter}'")
        print("✅ Your dataset has been updated for this specific letter/number")
    else:
        print(f"\n🎉 Data collection complete! Collected {end_class - start_class} classes.")
    
    print("\nNext steps:")
    print("1. Run: python create_real_dataset.py")
    print("2. Run: python train_classifier.py")
    print("3. Run: python sign_language_app.py")

if __name__ == "__main__":
    main()
