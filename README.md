# Real-Time Face Detection with OpenCV
This project demonstrates real-time face detection using OpenCV’s Haar Cascade classifier. The program leverages a webcam feed to detect faces dynamically, drawing green rectangles around detected faces and labeling them with customizable text.

---

## **Features**

### 🎥 Real-Time Face Detection
- Captures video feed from your webcam.
- Processes each frame to identify faces in real time.

### 🖍️ Visual Feedback
- Draws green rectangles around detected faces.
- Displays customizable labels above the rectangles.

### 🛑 User-Friendly Exit Mechanism
- Exit the program by pressing the `ESC` key directly in the OpenCV display window.

### ✏️ Customizable Parameters
- Modify text labels, detection sensitivity, and other parameters directly in the script.

---

## **How It Works**

1. **Capture Frames**: The program captures video frames from the webcam.
2. **Convert to Grayscale**: Each frame is converted to grayscale to simplify and speed up face detection.
3. **Detect Faces**: Uses the Haar Cascade classifier to detect faces in the grayscale image.
4. **Draw and Label**: Draws green rectangles around detected faces and labels them with customizable text.
5. **Display**: Shows the processed frames in real time in a dedicated OpenCV window.
6. **Exit**: Allows the user to quit by pressing the `ESC` key in the OpenCV window.

---

## **Getting Started**

### 🛠️ Prerequisites
To run this project, ensure you have the following:
- **Python 3.x**: A modern Python interpreter.
- **OpenCV Library**: Install it using:
  ```bash
  pip install opencv-python
  ```

### 📂 File Structure
- `face_detection.py`: The main Python script.
- `haarcascade_frontalface_default.xml`: The pre-trained Haar Cascade model for detecting faces. This file must be downloaded and placed in the same directory as the script.

---

## **Step-by-Step Instructions**

1. Clone this repository or download the project files.
2. Install the required Python libraries using the command:
   ```bash
   pip install opencv-python
   ```
3. Download the Haar Cascade file:
   - Get it from the [OpenCV GitHub repository](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml).
   - Save it in the same directory as the `face_detection.py` script.
4. Run the program using:
   ```bash
   python face_detection.py
   ```
5. To exit, press the `ESC` key on the OpenCV display window.

---

## **Expected Output**

When you run the program:
- A video feed from your webcam will appear.
- Detected faces will be surrounded by green rectangles labeled with "Face Detected" (or your customized text).
- The top-left corner will display "Press ESC to Exit" as an instruction.
---

## **Future Enhancements**
- Integrate YOLO for Advanced Object Detection
By integrating YOLO, the program can detect not just faces but also other objects like cars, animals, or household items. This makes the project more robust and versatile, suitable for applications like surveillance, retail analytics, or smart devices.
