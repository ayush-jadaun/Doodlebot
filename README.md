
# Ground Pattern Identification Bot

## Aim
This project leverages OpenCV, NumPy, and Python to create a bot capable of identifying and drawing patterns on the ground using an attached marker. The primary goal is to deliver robust pattern recognition and dynamic drawing capabilities for environments requiring real-time processing.

## Why?
Developed for MNNIT's Avishkar Tech Fest under the Robotics Club, this project addresses the challenges of real-time pattern detection and marker-based drawing. It supports both live camera feeds and static images, ensuring accurate marker detection and prompt responses during competitive events.

## Features
- **Real-time Pattern Identification:** Uses advanced computer vision techniques to process live image feeds and detect patterns.
- **Marker Tracking:** Accurately tracks an attached marker to determine the pattern's position.
- **Dynamic Pattern Drawing:** Automatically draws ground patterns based on detected marker positions.
- **Customizable Dictionary:** Easily update the internal dictionary to suit different marker types and images.
- **Optimized Performance:** Ensures minimal latency through efficient coding practices.

## Technologies Used
- **Python 3.x:** Core programming language.
- **OpenCV (opencv-contrib-python):** For image processing and computer vision operations.
- **NumPy:** For efficient numerical and array operations.

## Installation

### Prerequisites
- Ensure Python 3.x is installed.
- It is recommended to use a virtual environment for dependency management.

### Install Required Libraries
Install the necessary libraries using pip:

```bash
pip install numpy opencv-contrib-python
```

## Getting Started

1. **Clone the Repository:**
   - Fork this repository to your GitHub account.
   - Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. **Update File Directories:**
   - Modify file directories in the project if necessary, especially the paths for images or other required resources.

3. **Run the Python Project:**
   - For pattern detection, run the main Python script:
   ```bash
   python doodle.py
   ```
   - The program will prompt you to choose an input source:
     - **I**: Use an image file from the `images` folder.
     - **C**: Use the live camera feed.

## How It Works

1. **Image Acquisition:**  
   The bot captures images from a live camera feed or a stored image file.
2. **Preprocessing:**  
   Captured images are resized and processed using OpenCV and NumPy to enhance feature detection.
3. **Marker Detection and Pattern Recognition:**  
   The OpenCV ArUco module detects markers, whose positions are used to generate movement instructions for drawing patterns.
4. **Output and Visualization:**  
   The processed image displays the detected markers along with drawn patterns. Movement instructions are printed to the console.

## Arduino Integration

An integral part of the project is the Arduino sketch, now named **bot.ino**, which controls the doodle bot.

### Hardware Setup:
- Two DC motors controlled by a motor driver (e.g., L298N).
- Standard pin configurations are used in **bot.ino**.
- Preprogrammed directions can be set within **bot.ino** to automate movement, or the bot can receive live Serial commands from the Python script.

### Uploading **bot.ino**:
1. Open the **bot.ino** file in the Arduino IDE.
2. Connect your Arduino to your computer.
3. Select the appropriate board and COM port.
4. Upload the sketch.

### Python to Arduino Communication:
The Python script sends movement instructions (e.g., "Move Right", "Move Left") via serial communication to the Arduino. The Arduino sketch reads these commands and executes the corresponding motor movements (optimized for a 90° turn).

## Customization
- **Dictionary Updates:** Modify or update the internal pattern dictionary in the code if marker detection needs tuning.
- **Parameter Tuning:** Adjust thresholds and filters in OpenCV to accommodate different lighting or environmental conditions.
- **Input Source Options:** Toggle between a stored image and a live camera feed at runtime.

## Troubleshooting
- **Library Installation:** Ensure `numpy` and `opencv-contrib-python` are installed properly.
- **File Path Errors:** Verify that all paths in the code correspond to the correct locations of your images and other resources.
- **Camera Access Issues:** Ensure that the camera is properly connected and has the necessary permissions.
- **Arduino Communication:** Confirm that the correct COM port and baud rate (9600) are set in your Python script for serial communication with the Arduino.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a branch (e.g., `feature/YourFeature`).
3. Commit your changes (e.g., `git commit -am 'Add new feature'`).
4. Push your branch and open a pull request describing your changes.

Happy coding and happy pattern tracing!
