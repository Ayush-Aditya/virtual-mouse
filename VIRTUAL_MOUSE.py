import cv2
import mediapipe
import pyautogui

capture_hands = mediapipe.solutions.hands.Hands()
drawing_utils = mediapipe.solutions.drawing_utils
screen_width,screen_height=pyautogui.size()
camera = cv2.VideoCapture(0)
while True:
    ret, image = camera.read()
    image_height,image_width,_=image.shape
    if not ret:
        break

    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output_hands = capture_hands.process(rgb_image)
    all_hands = output_hands.multi_hand_landmarks
    if all_hands:
        for hand_landmarks in all_hands:
            drawing_utils.draw_landmarks(image, hand_landmarks, mediapipe.solutions.hands.HAND_CONNECTIONS)
            one_hand_landmark=hand_landmarks.landmark
            for id,lm in enumerate(one_hand_landmark):
              x=int(lm.x*image_width)
              y=int(lm.y*image_height)
             # print(x,y)
              if id==8:
                  mouse_x=int(screen_width/image_width*x)
                  mouse_y=int(screen_height/image_height*y)
                  cv2.circle(image,(x,y),10,(0,225,255))
                  pyautogui.moveTo(mouse_x,mouse_y)
                  x1=x
                  y1=y
              if id==4 :
                  cv2.circle(image,(x,y),10,(0,255,255)) 
                  x2=x
                  y2=y   
        dist=y2-y1
        print(dist)
        if(dist<20):
            pyautogui.click()
        
    cv2.imshow("Hand movement video capture", image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
