import cv2
import mediapipe as mp
from hand import Hand
from gesture import Gesture
import pyautogui
import os
import logging

# Suppress TensorFlow Lite warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
logging.getLogger('tensorflow').setLevel(logging.ERROR)

# Disable the fail-safe
pyautogui.FAILSAFE = False

# Initialize camera with error checking
cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)

# Check if camera opened successfully
if not cap.isOpened():
    print("\n" + "="*50)
    print("ERROR: Cannot access camera!")
    print("="*50)
    print("Please check the following:")
    print("1. Camera privacy settings (Windows Settings → Privacy & security → Camera)")
    print("2. Close other apps using camera (Skype, Teams, Zoom, Camera app)")
    print("3. Camera drivers are properly installed")
    print("4. Try unplugging and reconnecting USB camera")
    print("5. Restart your computer if the issue persists")
    print("="*50)
    input("Press Enter to exit...")
    exit()

# Set camera properties for better performance
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

print("Camera initialized successfully!")
print(f"Camera resolution: {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}x{int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}")

hand_detector = mp.solutions.hands.Hands() # create a hand detector object
drawing_utils = mp.solutions.drawing_utils # create a drawing utils object

hand_left = Hand("Left")
hand_right = Hand("Right")
gesture = Gesture(hand_left, hand_right)

while True:
    ret, frame = cap.read() # read a frame
    
    # Check if frame was read successfully
    if not ret:
        print("ERROR: Could not read frame from camera")
        break
        
    frame = cv2.flip(frame, 1) # flip the frame
    frame_height, frame_width, _ = frame.shape # get the frame height and width
    gesture.setFrame(frame) # set the frame for gesture

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # convert the frame to RGB
    output = hand_detector.process(rgb_frame) # process the frame
    hands = output.multi_hand_landmarks # get the landmarks of the hand
    handedness = output.multi_handedness  # get the handedness information

    if hands and handedness: # if hands is detected
        for hand_landmarks, hand_handedness in zip(hands, handedness):
            hand_label = hand_handedness.classification[0].label  # 'Left' or 'Right'
            drawing_utils.draw_landmarks(frame, hand_landmarks)  # draw the landmarks on the frame

            if hand_label == 'Left':
                hand_left.update_landmarks(hand_landmarks.landmark, frame) # update the landmarks for left hand
            else:
                hand_right.update_landmarks(hand_landmarks.landmark, frame) # update the landmarks for right hand

            gesture.readCoordinates() # read the coordinates of the hands
    else:
        hand_left.reset_landmarks()  # reset coordinates for left hand
        hand_right.reset_landmarks()  # reset coordinates for right hand
        gesture.reset() # reset the gesture

    cv2.imshow('Virtual Mouse', frame) # display the frame

    if not gesture.active or cv2.waitKey(1) & 0xFF == ord('q'): # press q to quit
        break

cap.release()
cv2.destroyAllWindows()