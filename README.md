# PushUps-Counter
 This project is a real-time push-up counter that uses Python, OpenCV, and MediaPipe Pose Estimation to track and count push-ups using a webcam. The program detects body landmarks, tracks motion, and increments the counter when a full push-up is completed.

## How It Works  
- **Capture Video** – The webcam captures a live video stream.  
- **Detect Landmarks** – MediaPipe Pose detects key body points (shoulders, elbows, wrists).  
- **Analyze Movement** – The program determines if the body is in an "up" or "down" position.  
- **Count Push-Ups** – A push-up is counted when the user moves from "down" to "up."  
- **Display Counter** – The push-up count is displayed in real-time on the screen.  

## Technologies Used  
- **Python** – Core programming language.  
- **OpenCV** – For image processing and real-time video capture.  
- **MediaPipe** – AI-powered pose detection for body landmark tracking.  

## Installation & Setup  
### Prerequisites  
Ensure you have **Python** installed on your system. Then, install the required dependencies:  
```bash
pip install opencv-python mediapipe
