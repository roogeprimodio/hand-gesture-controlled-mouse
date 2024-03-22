# Hand Gesture Controlled Mouse

This is a Python application that allows you to control the mouse cursor using hand gestures detected by a webcam. It utilizes the Mediapipe library for hand tracking and PyAutoGUI for mouse control.

## Features

- Control the mouse cursor with hand gestures.
- Detects the tip of the index finger to move the cursor.
- Left-click by bringing the index finger and middle finger close together.

## Requirements

- Python 3.11
- OpenCV
- Mediapipe
- PyAutoGUI

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/roogeprimodio/hand-gesture-controlled-mouse.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the `aimouse.py` script:

    ```bash
    python aimouse.py
    ```

2. A window will open displaying the webcam feed. Perform hand gestures in front of the webcam to control the mouse cursor.

3. Bring the index finger and middle finger close together to perform a left-click.

4. The cursor movements will be logged in the command line.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
