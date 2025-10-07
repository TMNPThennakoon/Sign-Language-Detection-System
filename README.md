# Sign Language Detector

A modern, user-friendly sign language detection application built with Python, OpenCV, and MediaPipe.

## Author
**Nayana Pabasara** - Developer & Creator

## Features
- Real-time sign language recognition using hand landmarks
- Modern GUI interface with custom styling
- Easy data collection for training custom gestures
- Machine learning model training and inference
- Support for complete alphanumeric recognition: 26 English letters (A-Z) + 10 numbers (0-9)

## Technologies Used
- Python 3.x
- OpenCV for computer vision
- MediaPipe for hand tracking
- Scikit-learn for machine learning
- Tkinter for GUI interface

## Installation

1. Clone this repository
2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. **Data Collection**: Run `collect_imgs.py` to collect training images
2. **Dataset Creation**: Run `create_dataset.py` to process collected images
3. **Model Training**: Run `train_classifier.py` to train the ML model
4. **Real-time Detection**: Run `sign_language_app.py` for the GUI application

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
