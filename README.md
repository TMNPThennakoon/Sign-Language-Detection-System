# 🤟 Sign Language Detection System



<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8.0-green?style=for-the-badge&logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.13-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A modern, intelligent sign language detection system that recognizes all 36 alphanumeric symbols (A-Z + 0-9) in real-time using computer vision and machine learning.**

[![GitHub stars](https://img.shields.io/github/stars/TMNPThennakoon/Sign-Language-Detection-System?style=social)](https://github.com/TMNPThennakoon/Sign-Language-Detection-System)
[![GitHub forks](https://img.shields.io/github/forks/TMNPThennakoon/Sign-Language-Detection-System?style=social)](https://github.com/TMNPThennakoon/Sign-Language-Detection-System)

</div>

---

## 👨‍💻 Author
**Nayana Pabasara** - Developer & Creator  
*Building accessible technology for the deaf and hard-of-hearing community*

---
![IMG_6966](https://github.com/user-attachments/assets/197c696d-7e82-4fb1-8e64-bd8322570f85)

## ✨ User Interface

![Image 2025-10-07 at 13 00](https://github.com/user-attachments/assets/0922181c-d473-4a0e-a969-f4881d54a7fd)
<center>**Sign Language Detector Main UI**</center>

![Image 2025-10-07 at 12 59](https://github.com/user-attachments/assets/91e3c3f7-479a-4724-8eb5-6739b76b209d)
<center>**Sign Language Data Collector UI**</center>

---
## ✨ Features

### 🎯 **Core Capabilities**
- 🤖 **Real-time Recognition** - Instant detection of hand gestures using advanced computer vision
- 🎨 **Modern GUI Interface** - Sleek dark-themed interface with custom styling and intuitive controls
- 📊 **Complete Alphanumeric Support** - All 26 English letters (A-Z) + 10 numbers (0-9)
- 🧠 **Smart Machine Learning** - Random Forest classifier with 90%+ accuracy
- 📱 **Live Camera Feed** - Real-time video processing with hand landmark visualization

### 🚀 **Advanced Features**
- 🎯 **Targeted Data Collection** - Update individual letter datasets without retraining everything
- 📈 **Interactive Progress Tracking** - Real-time status updates and collection progress
- 🔧 **Flexible Training Pipeline** - Easy model training and inference
- 🎪 **Batch Collection Options** - Collect all letters, numbers, or specific symbols
- 📚 **Comprehensive Documentation** - Complete guides for all 36 symbols

### 🛠️ **Technical Highlights**
- **42 Hand Landmarks** - Precise feature extraction using MediaPipe
- **Custom Feature Engineering** - Normalized relative coordinates for robust recognition
- **Cross-platform Compatibility** - Works on Windows, macOS, and Linux
- **Modular Architecture** - Clean, maintainable codebase with separation of concerns

---

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| 🐍 **Python** | Core programming language | 3.x |
| 👁️ **OpenCV** | Computer vision and image processing | 4.8.0+ |
| 🤖 **MediaPipe** | Hand tracking and landmark detection | 0.10.13+ |
| 🧠 **Scikit-learn** | Machine learning algorithms | 1.3.0+ |
| 🖥️ **Tkinter** | GUI interface development | Built-in |
| 📊 **NumPy** | Numerical computing | 1.21.0+ |
| 🖼️ **Pillow** | Image processing | 8.3.0+ |

---

## 🚀 Quick Start

### 📋 Prerequisites
- Python 3.7 or higher
- Webcam or camera device
- 4GB+ RAM recommended

---

## 📖 Usage Guide

### 🎯 **Step 1: Data Collection**
```bash
python collect_imgs.py
```
- **Interactive Menu**: Choose specific letters, numbers, or batch collection
- **Smart Validation**: Input validation for letter/number selection
- **Progress Tracking**: Real-time collection progress with visual feedback

### 🔄 **Step 2: Dataset Creation**
```bash
python create_dataset.py
```
- **Feature Extraction**: Automated MediaPipe landmark processing
- **Data Preprocessing**: Normalization and feature engineering
- **Quality Control**: Validation of collected data

### 🧠 **Step 3: Model Training**
```bash
python train_classifier.py
```
- **Random Forest Training**: Optimized hyperparameters
- **Cross-validation**: Robust model evaluation
- **Performance Metrics**: Accuracy, precision, and recall

### 🎪 **Step 4: Real-time Detection**
```bash
python sign_language_app.py
```
- **Live Detection**: Real-time gesture recognition
- **Visual Feedback**: Bounding boxes and predictions
- **Status Monitoring**: Real-time system status

---

## 📁 Project Structure

```
Sign-Language-Detection-System/
├── 🤖 sign_language_app.py      # Main GUI application
├── 📸 collect_imgs.py           # Data collection with letter selection
├── 🔄 create_dataset.py         # Dataset creation and processing
├── 🧠 train_classifier.py       # Model training pipeline
├── 🔮 inference_classifier.py  # Prediction inference
├── 🚀 run_app.bat              # Windows launcher
├── 📋 requirements.txt          # Python dependencies
├── 📖 README.md                # Project documentation
├── 📄 LICENSE                  # MIT License
├── 🚫 .gitignore               # Git ignore rules
└── 📚 Documentation/
    ├── COMPLETE_ALPHANUMERIC_GUIDE.md
    └── DATA_COLLECTION_GUIDE.md
```

---

## 🎯 Supported Symbols

### 📝 **Letters A-Z (Classes 0-25)**
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z

### 🔢 **Numbers 0-9 (Classes 26-35)**
0, 1, 2, 3, 4, 5, 6, 7, 8, 9

---

## 🎨 Screenshots & Demo

### 🖥️ **Main Application Interface**
- Modern dark-themed GUI
- Real-time camera feed
- Live detection results
- Status monitoring panel

### 📊 **Data Collection Interface**
- Interactive letter selection
- Progress tracking
- Smart validation
- Batch collection options

---

## 🔧 Advanced Configuration

### 🎯 **Targeted Letter Collection**
Update specific letters without retraining the entire model:
```bash
python collect_imgs.py
# Select "Collect Specific Letter/Number"
# Enter letter (e.g., "G")
# Collect 40 new images for that letter
```

### 📊 **Model Performance Tuning**
- Adjust confidence thresholds
- Modify feature extraction parameters
- Customize training hyperparameters

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### 🐛 **Bug Reports**
- Use GitHub Issues for bug reports
- Include system information and error logs
- Provide steps to reproduce

### 💡 **Feature Requests**
- Suggest new features via GitHub Issues
- Describe use cases and benefits
- Consider implementation complexity

---

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| **Accuracy** | 90%+ |
| **Processing Speed** | 30 FPS |
| **Memory Usage** | <500MB |
| **Model Size** | <10MB |
| **Training Time** | 5-10 minutes |

---

## 🌟 Use Cases

### 🎓 **Educational**
- Sign language learning and practice
- Educational institutions teaching ASL
- Interactive learning applications

### ♿ **Accessibility**
- Communication tools for deaf individuals
- Assistive technology development
- Accessibility research projects

### 🔬 **Research**
- Computer vision research
- Machine learning experiments
- Human-computer interaction studies

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 T.M.N.P.Thennakoon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

- **MediaPipe Team** - For the excellent hand tracking solution
- **OpenCV Community** - For computer vision capabilities
- **Scikit-learn Team** - For machine learning algorithms
- **Python Community** - For the amazing ecosystem


---

<div align="center">

**🌟 If this project helped you, please give it a star! 🌟**

[![GitHub stars](https://img.shields.io/github/stars/TMNPThennakoon/Sign-Language-Detection-System?style=social)](https://github.com/TMNPThennakoon/Sign-Language-Detection-System)
[![GitHub forks](https://img.shields.io/github/forks/TMNPThennakoon/Sign-Language-Detection-System?style=social)](https://github.com/TMNPThennakoon/Sign-Language-Detection-System)

**Building technology that makes communication more accessible, one gesture at a time! 🤟**

</div>
