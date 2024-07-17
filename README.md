# Hand Gesture Control

This project uses hand gestures to control mouse actions such as moving the pointer, clicking, holding, and right-clicking. The project utilizes OpenCV, MediaPipe, and PyAutoGUI libraries to detect hand gestures and perform corresponding mouse actions.

## Installation

Follow these steps to set up the environment and run the project.

### Prerequisites

Make sure you have Python installed. This project was tested with Python 3.x.

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/zirvu/hand-gesture-control.git
cd hand-gesture-control
```

### Step 2: Install Required Packages

Install the required Python packages using pip:

1. **OpenCV**: OpenCV is used for video capture and frame processing.

   ```bash
   pip install opencv-python
   ```

2. **MediaPipe**: MediaPipe is used for hand landmark detection.

   ```bash
   pip install mediapipe
   ```

3. **PyAutoGUI**: PyAutoGUI is used for controlling mouse actions.

   ```bash
   pip install pyautogui
   ```

### Step 3: Run the Project

Navigate to the project directory and run the main script:

```bash
python main.py
```

## Project Structure

- `hand.py`: Contains the `Hand` which manages the hand landmarks.
- `main.py`: The main script that captures video frames, detects hand landmarks, and performs gestures.
- `gesture.py`: Contains the `Gesture` class that defines various mouse control actions based on hand gestures.

## Usage

- **Pointer Movement**: Move the right hand's index finger to move the mouse pointer.
- **Left Click**: Bring the right hand's thumb and index finger close together to perform a left click.
- **Hold Left Click**: Bring the right hand's thumb close to the base of the index finger to hold the left click.
- **Right Click**: Bring the right hand's thumb and ring finger close together to perform a right click.
- **Middle Click**: Bring the right hand's thumb and middle finger close together to perform a middle click.
- **Hold Middle Click**: Bring the right hand's thumb close to the base of the middle finger to hold the middle click.
- **Scroll**: Bring the right hand's thumb and middle PIP joint close together to toggle scroll mode. Move the right hand's index finger up or down to scroll.
- **Quit**: Bring the left hand's index finger close to the right hand's wrist to quit the application.

## Contributing

Feel free to fork this repository, make your changes, and submit a pull request. Contributions are welcome!
