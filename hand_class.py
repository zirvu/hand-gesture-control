import cv2
import pyautogui

class HandClass:
    class Landmark:
        def __init__(self, label):
            self.label = label
            self.landmark_x = 0
            self.landmark_y = 0
            self.x = 0
            self.y = 0

    def __init__(self, label):
        self.screen_width, self.screen_height = pyautogui.size()
        self.label = label
        self.frame = None
        self.landmarks = [
            self.Landmark("wrist"),
            self.Landmark("thumb_cmc"),
            self.Landmark("thumb_mcp"),
            self.Landmark("thumb_ip"),
            self.Landmark("thumb_tip"),
            self.Landmark("index_finger_mcp"),
            self.Landmark("index_finger_pip"),
            self.Landmark("index_finger_dip"),
            self.Landmark("index_finger_tip"),
            self.Landmark("middle_finger_mcp"),
            self.Landmark("middle_finger_pip"),
            self.Landmark("middle_finger_dip"),
            self.Landmark("middle_finger_tip"),
            self.Landmark("ring_finger_mcp"),
            self.Landmark("ring_finger_pip"),
            self.Landmark("ring_finger_dip"),
            self.Landmark("ring_finger_tip"),
            self.Landmark("pinky_mcp"),
            self.Landmark("pinky_pip"),
            self.Landmark("pinky_dip"),
            self.Landmark("pinky_tip"),
        ]

    def update_landmarks(self, landmarks, frame):
        self.frame = frame
        frame_height, frame_width, _ = self.frame.shape

        for i, landmark in enumerate(landmarks):
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            self.landmarks[i].landmark_x = x
            self.landmarks[i].landmark_y = y
            self.landmarks[i].x = self.screen_width / frame_width * x
            self.landmarks[i].y = self.screen_height / frame_height * y

    def reset_landmarks(self):
        for landmark in self.landmarks:
            landmark.landmark_x = 0
            landmark.landmark_y = 0
            landmark.x = 0
            landmark.y = 0