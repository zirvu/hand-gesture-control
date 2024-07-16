import cv2
import pyautogui

class Gesture:
    def __init__(self, hand_left, hand_right):
        self.active = True
        self.frame = None
        self.hand_left = hand_left
        self.hand_right = hand_right

        self.can_move_pointer = True
        self.hold_left_click = False
        self.hold_middle_click = False
        self.is_scroll = False

    def setFrame(self, frame):
        self.frame = frame

    def readCoordinates(self):
        self.pointer()
        self.leftClick()
        self.holdLeftClick()
        self.middleClick()
        self.holdMiddleClick()
        self.activeScroll()
        self.rightClick()

        self.checkQuit()

    def pointer(self):
        index_right_tip = self.hand_right.landmarks[8]
        cv2.circle(
            img=self.frame, 
            center=(index_right_tip.landmark_x, index_right_tip.landmark_y), 
            radius=10, 
            color=(0, 255, 0),
        )
        if self.can_move_pointer and self.hand_right.active:
            pyautogui.moveTo(index_right_tip.x, index_right_tip.y) # move the mouse pointer to the tip of the index finger
        
        if self.is_scroll and self.hand_right.active:
            if index_right_tip.y < self.frame.shape[0] // 2:
                pyautogui.scroll(50)
            else:
                pyautogui.scroll(-50)
    
    def leftClick(self):
        thumb_right_tip = self.hand_right.landmarks[4]
        index_right_tip = self.hand_right.landmarks[8]

        cv2.circle(
            img=self.frame, 
            center=(thumb_right_tip.landmark_x, thumb_right_tip.landmark_y), 
            radius=10, 
            color=(0, 255, 0),
        )
        
        if not self.is_scroll and self.hand_right.active:
            if abs(index_right_tip.x - thumb_right_tip.x) < 30 and abs(index_right_tip.y - thumb_right_tip.y) < 30:
                pyautogui.click() # click the mouse
                pyautogui.sleep(1) # sleep for 1 seconds

    def holdLeftClick(self):
        thumb_right_tip = self.hand_right.landmarks[4]
        index_right_mcp = self.hand_right.landmarks[5]

        if not self.is_scroll and self.hand_right.active:
            if abs(thumb_right_tip.x - index_right_mcp.x) < 15 and abs(thumb_right_tip.y - index_right_mcp.y) < 15:
                self.hold_left_click = not self.hold_left_click
                if self.hold_left_click:
                    pyautogui.mouseDown() # hold the left click of the mouse
                else:
                    pyautogui.mouseUp() # release the left click of the mouse
                pyautogui.sleep(1) # sleep for 1 seconds

    def middleClick(self):
        thumb_right_tip = self.hand_right.landmarks[4]
        middle_right_tip = self.hand_right.landmarks[12]

        cv2.circle(
            img=self.frame, 
            center=(middle_right_tip.landmark_x, middle_right_tip.landmark_y), 
            radius=10, 
            color=(0, 255, 0),
        )
        
        if not self.is_scroll and self.hand_right.active:
            if abs(thumb_right_tip.x - middle_right_tip.x) < 30 and abs(thumb_right_tip.y - middle_right_tip.y) < 30:
                pyautogui.click(button='middle') # click the middle button of the mouse

    def holdMiddleClick(self):
        thumb_right_tip = self.hand_right.landmarks[4]
        middle_right_mcp = self.hand_right.landmarks[9]

        if not self.is_scroll and self.hand_right.active:
            if abs(thumb_right_tip.x - middle_right_mcp.x) < 15 and abs(thumb_right_tip.y - middle_right_mcp.y) < 15:
                self.hold_middle_click = not self.hold_middle_click
                if self.hold_middle_click:
                    pyautogui.mouseDown(button='middle') # hold the middle click of the mouse
                else:
                    pyautogui.mouseUp(button='middle') # release the middle click of the mouse
                pyautogui.sleep(1) # sleep for 1 seconds

    def activeScroll(self):
        thumb_right_tip = self.hand_right.landmarks[4]
        middle_right_pip = self.hand_right.landmarks[10]

        if self.hand_right.active:
            if abs(thumb_right_tip.x - middle_right_pip.x) < 10 and abs(thumb_right_tip.y - middle_right_pip.y) < 10:
                self.is_scroll = not self.is_scroll
                self.can_move_pointer = not self.is_scroll
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

        if not self.is_scroll and self.hand_right.active:
            if abs(thumb_right_tip.x - ring_right_tip.x) < 30 and abs(thumb_right_tip.y - ring_right_tip.y) < 30:
                pyautogui.rightClick() # right click the mouse

    def checkQuit(self):
        index_left_tip = self.hand_left.landmarks[8]
        wrist_right = self.hand_right.landmarks[0]

        if abs(index_left_tip.x - wrist_right.x) < 15 and abs(index_left_tip.y - wrist_right.y) < 15:
            # pyautogui.hotkey('alt', 'f4')
            self.active = False

    def reset(self):
        self.can_move_pointer = True
        self.is_scroll = False
        
        if self.hold_left_click:
            self.hold_left_click = False
            pyautogui.mouseUp()

        if self.hold_middle_click:
            self.hold_middle_click = False
            pyautogui.mouseUp(button='middle')
