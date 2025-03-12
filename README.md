# Virtual Mouse and Gesture Control



## 🚀 Overview
The **Virtual Mouse and Gesture Control** project enables seamless, touch-free interaction with a computer using hand gestures detected by **MediaPipe**. It simulates a real mouse, allowing users to navigate, click, and control their system with intuitive hand movements. 

Additionally, the project expands into gesture-based gaming controls and presentation navigation, providing a hands-free experience for various applications.

## 🔥 Features
- 🎯 **Hand Tracking with MediaPipe**: Detects hand landmarks and tracks movements.
- 🖱 **Virtual Mouse Control**: Move the cursor and perform clicks using hand gestures.
- 🎮 **Game Control**: Play racing games with W, A, S, D gestures.
- 📊 **Gesture-Based Presentation Control**: Navigate slides and zoom in/out using gestures.
- 📱 **DroidCam Integration**: Use a smartphone as an external webcam.
- ⚡ **Fast and Lightweight**: Efficient implementation using Python and OpenCV.

## 📂 Project Files
### 1️⃣ `VIRTUAL_MOUSE.py`
- Uses **MediaPipe** for hand tracking.
- Adjusts hand landmarks to screen dimensions.
- Detects finger distances to simulate mouse clicks.
- Cursor dynamically follows the **index finger**.

### 2️⃣ `gamevirtual.py`
- Adapts gesture detection for controlling keyboard inputs.
- Implements **W, A, S, D** controls for racing games.
- Uses **DroidCam** for smartphone-based webcam functionality.

### 3️⃣ `Gesturecontrolledslide.py`
- Enables gesture-controlled **slide navigation**.
- Supports actions like **zooming and paging** during presentations.

## 🛠 Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/Ayush-Aditya/virtual-mouse.git
   cd virtual-mouse
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Virtual Mouse**
   ```bash
   python VIRTUAL_MOUSE.py
   ```

## 📌 Requirements
- Python 3.7+
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

## 🎯 Target Audience
This project is ideal for:
✅ **Tech Enthusiasts & Developers** exploring gesture recognition.
✅ **Gamers** looking for an immersive hands-free experience.
✅ **Presenters & Educators** who want smooth slide navigation.
✅ **Accessibility Advocates** improving human-computer interaction.

## 💡 Commercial Potential
- 🤖 **Human-Computer Interaction**: Future of touchless interfaces.
- 🎮 **Gaming Industry**: Enhancing immersive experiences.
- 🔍 **Assistive Technology**: Empowering users with disabilities.



## 👨‍💻 Author
**Ayush Aditya**  
📌 [GitHub](https://github.com/Ayush-Aditya) | 📌 [LinkedIn](https://www.linkedin.com/in/ayush-aditya-link-kedin/)

## 📜 License
This project is licensed under the **MIT License**. Feel free to use and enhance it!

---
🌟 *If you like this project, don't forget to star ⭐ the repository!*
