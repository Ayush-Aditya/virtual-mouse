Virtual Mouse and Gesture Control
This project is designed to simulate a real mouse using hand gestures detected by MediaPipe, enabling seamless virtual control. Initially, the project utilizes MediaPipe’s hand gesture detection to track hands and control the mouse on a screen. PyAutoGUI is then employed to interact with the GUI interface of the machine.

In the second stage, the project incorporates gesture detection via neural networks, which are linked to PyAutoGUI's hotkey functionality, enriching the mouse's feature set with additional capabilities.

Project Files
VIRTUAL_MOUSE.py: This script leverages MediaPipe to detect hand landmarks and adjust them to the screen’s height and width. It calculates the distance between various fingers to trigger different actions, such as clicking. The mouse pointer dynamically follows the index finger across the screen.

gamevirtual.py: This file adapts the same gesture detection principles to control keyboard inputs, enabling W, A, S, D commands for car racing games. By utilizing a webcam, users can control racing games using hand gestures. The code includes integration with DroidCam, allowing a smartphone to be used as an external webcam.

Gesturecontrolledslide.py: This script enables gesture-based control during presentations and public demonstrations. Users can perform actions like zooming, paging up or down, and more—simply using hand gestures in front of a webcam.

Target Audience and Commercial Value
This project is ideal for tech enthusiasts, developers, and researchers interested in exploring the capabilities of gesture recognition technology. It targets individuals looking to enhance user experience in gaming, virtual mouse control, and presentation environments.

Commercially, the code holds significant potential for companies in the fields of human-computer interaction, gaming, and assistive technology. It offers innovative solutions for hands-free control, improving accessibility and providing a futuristic approach to interacting with digital environments. As gesture recognition becomes increasingly integral in various industries, this project serves as a valuable resource for developing cutting-edge, user-friendly interfaces.
