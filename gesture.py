import cv2
import pyautogui

class Gesture:
    def __init__(self, hand_left, hand_right):
        self.frame = None
        self.hand_left = hand_left
        self.hand_right = hand_right
        self.hold_left_click = False

    def setFrame(self, frame):
        self.frame = frame

    def readCoordinates(self):
        self.pointer()
        self.leftClick()
        self.holdLeftClick()
        self.rightClick()

    def pointer(self):
        index_right_tip = self.hand_right.landmarks[8]
        cv2.circle(
            img=self.frame, 
            center=(index_right_tip.landmark_x, index_right_tip.landmark_y), 
            radius=10, 
            color=(0, 255, 0),
        )
        pyautogui.moveTo(index_right_tip.x, index_right_tip.y) # move the mouse pointer to the tip of the index finger
    
    def leftClick(self):
        thumb_right_tip = self.hand_right.landmarks[4]
        index_right_tip = self.hand_right.landmarks[8]

        cv2.circle(
            img=self.frame, 
            center=(thumb_right_tip.landmark_x, thumb_right_tip.landmark_y), 
            radius=10, 
            color=(0, 255, 0),
        )

        if abs(index_right_tip.x - thumb_right_tip.x) < 30 and abs(index_right_tip.y - thumb_right_tip.y) < 30:
            pyautogui.click() # click the mouse
            pyautogui.sleep(1) # sleep for 1 seconds

    def holdLeftClick(self):
        thumb_right_tip = self.hand_right.landmarks[4]
        index_right_mcp = self.hand_right.landmarks[5]

        if abs(thumb_right_tip.x - index_right_mcp.x) < 15 and abs(thumb_right_tip.y - index_right_mcp.y) < 15:
            self.hold_left_click = not self.hold_left_click
            print(self.hold_left_click)
            if self.hold_left_click:
                pyautogui.mouseDown() # hold the left click of the mouse
            else:
                pyautogui.mouseUp() # release the left click of the mouse
            pyautogui.sleep(1) # sleep for 1 seconds

    def rightClick(self):
        thumb_right_tip = self.hand_right.landmarks[4]
        ring_right_tip = self.hand_right.landmarks[16]

        cv2.circle(
            img=self.frame, 
            center=(ring_right_tip.landmark_x, ring_right_tip.landmark_y), 
            radius=10, 
            color=(0, 255, 0),
        )

        if abs(thumb_right_tip.x - ring_right_tip.x) < 30 and abs(thumb_right_tip.y - ring_right_tip.y) < 30:
            pyautogui.rightClick() # right click the mouse

    def reset(self):
        self.hold_left_click = False
        pyautogui.mouseUp()