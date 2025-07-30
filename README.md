# Driver Drowsiness Detection on Raspberry Pi

A lightweight, real-time driver alertness system that uses a camera and OpenCV's Haar Cascade classifiers to detect closed eyes and warn the driver, helping prevent drowsiness-related accidents.

## 🚗 How it Works

- Continuously monitors the driver’s eyes using a camera (USB webcam or Pi Camera Module).
- If eyes are not detected for **3 seconds or more**, an audio alert sounds to draw the driver’s attention back to the road.
- Designed for efficient real-time performance on Raspberry Pi 3 or newer, running Raspberry Pi OS (Raspbian).

## 📷 Hardware Requirements

- **Raspberry Pi 3 or newer** (e.g., Pi 3, Pi 4)
- **Raspberry Pi OS (Raspbian)**
- **USB webcam** or official **Pi Camera Module**
- **Speakers or earphones** for audio output

## 🛠️ Software Requirements

- **Python 3.x** (pre-installed on Raspberry Pi OS)
- **OpenCV** (`opencv-python` for Python)
- **playsound** Python package

## 🔗 Haar Cascade Classifier Resource

Download [haarcascade_eye.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml):


Place `haarcascade_eye.xml` in the project directory.

## 🔔 Audio Alert

Place an MP3 file named `eyess.mp3` (with a loud warning sound or a voice prompt like “Please wake up and focus on the road!”) in the same directory.  
You can record your own or use a free sound from sites like [Freesound](https://freesound.org/).

## 🔧 Installation

1. Update your package manager and install dependencies:
    ```
    sudo apt-get update
    sudo apt-get install python3-pip python3-opencv
    pip3 install playsound
    ```

2. Download the required Haar Cascade file:
    ```
    wget https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_eye.xml
    ```

3. Ensure your audio alert file is named `eyess.mp3` in your project folder.

4. Connect your webcam or Pi Camera Module (and enable the camera interface in `raspi-config` if using Pi Camera).

## 🚀 Running the App

In the terminal, run:

python main.py


- The webcam feed will start.
- If your eyes are closed (or not detected) for 3 seconds, the alert will play.
- Press `q` to quit.

## 🧠 How is Drowsiness Detected?

- Each video frame checks for eyes using the Haar Cascade classifier.
- If fewer than 2 eyes are found across frames, a timer starts.
- If low-eye-detection persists for more than 3 seconds, the MP3 alarm is triggered.
- The system resets once eye(s) are again detected.

## 👨‍🔧 Performance and Tips

- Haar Cascade is extremely efficient and runs smoothly on Pi 3+.
- For best results:
  - Use in well-lit environments.
  - Mount the camera securely, facing the driver.
  - Use loud and clear audio alerts.
- No additional sensors or hardware integrations required.

## 🌟 Adaptation Ideas

- Integrate with vehicle ignition/interlock for extra safety.
- Log detection timestamps for safety analytics.
- Extend to include face detection, head pose estimation, or deep learning-based eye status detection if more accuracy is desired.

## 📎 References

- [OpenCV Haar Cascade documentation](https://docs.opencv.org/master/d7/d8b/tutorial_py_face_detection.html)
- [Official Haar Cascade XML Files](https://github.com/opencv/opencv/tree/master/data/haarcascades)
- [Raspberry Pi Camera docs](https://www.raspberrypi.com/documentation/accessories/camera.html)

---

**Drive safe! This project is for educational and prototyping purposes—not a substitute for professional-grade safety systems.**
