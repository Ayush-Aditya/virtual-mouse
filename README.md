This project has been developed to imitate a real mouse in the first stage, it only uses media pipe hand gesture detection to detect the hands, which are used to control the mouse virtually.
It uses pyautogui to interact with the GUI interface of the machine.
In the second stage, I will be working on gesture detection using LSTM ((RNN) recurrent neural network) and bind those gestures with the hotkey feature of pygautogui to make the mouse feature rich.

The main file VIRTUAL_MOUSE.py uses media pipe gesture detection to find the hand's landmark which is adjusted to the screen height and width. After that, the code uses the distance between different fingers to perform various tasks like clicking. The mouse pointer always moves along the index finger to any point on the screen.

The second file gamevirtual.py uses the same principle and keyboard-controlling libraries to perform the W,A,S,D control for CAR RACING games. With the help of this one can play car racing games using hand a webcam. In the real code droidcam is used to make cellphone as an external webcam.
