
# Ground Pattern Identification Bot

## Aim
This project uses OpenCV, NumPy, and Python to create a bot capable of identifying and drawing patterns on the ground using an attached marker. The primary goal is to facilitate robust pattern recognition and enable dynamic drawing based on detected ground features.

## Why?
This project was developed for MNNIT's Avishkar Tech Fest under the Robotics Club. It was designed to meet the challenges of real-time pattern detection and drawing during the competition. I was responsible for developing the software, focusing on leveraging computer vision techniques to accurately identify and respond to marker inputs.

## Features
- **Real-time Pattern Identification:** Utilizes OpenCV and NumPy to recognize and identify patterns from live image feeds.
- **Marker Tracking:** Detects and tracks an attached marker to assist in drawing accurate patterns.
- **Dynamic Pattern Drawing:** Automatically draws patterns on the ground based on the identified marker placements.
- **Customizable Dictionary:** Easily update the pattern dictionary within the code to suit different images or marker types.
- **Optimized Performance:** Designed for real-time processing, ensuring responsiveness during live operations.

## Technologies Used
- **Python 3.x:** The core programming language used.
- **OpenCV:** For image processing and computer vision tasks.
- **NumPy:** For efficient numerical computations and array processing.

## Installation

### Prerequisites
- Python 3.x must be installed on your machine.
- A virtual environment is recommended for dependency management.

### Install Required Libraries
Use the following command to install the necessary libraries:

```bash
pip install numpy opencv-contrib-python
```

## Getting Started

1. **Fork and Clone the Repository:**
   - Fork this repository to your GitHub account.
   - Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. **Update File Directories:**
   - Open the project files and update the image directories or any other necessary file paths as required for your setup.

3. **Run the Project:**
   - Navigate to the project directory and run the main script (replace `main.py` with your entry file if different):

   ```bash
   python doodle.py
   ```

## How It Works
1. **Image Acquisition:**  
   The bot captures images or video frames using an attached camera.

2. **Preprocessing:**  
   The acquired images are processed using OpenCV and NumPy for filtering, edge detection, and other enhancements to prepare for pattern identification.

3. **Pattern Recognition:**  
   The preprocessed images are compared against a predefined dictionary of patterns. If the marker is detected, the relevant pattern is identified.

4. **Drawing Patterns:**  
   Based on the detected pattern and marker position, the bot dynamically draws the corresponding pattern on the ground.

## Customization
- **Dictionary Updates:**  
  If the bot does not correctly identify patterns for your chosen image, update the dictionary values in the source code accordingly.
  
- **Parameter Tuning:**  
  Modify OpenCV parameters such as thresholds and filters to optimize performance based on your specific hardware and environmental factors.

## Troubleshooting
- **Library Installation Issues:**  
  Ensure that all required libraries are installed and updated.
  
- **File Directory Problems:**  
  Verify that the file directories in your code are correctly pointing to the actual locations of your images and other resources.
  
- **Environmental Factors:**  
  Adequate lighting and a stable camera setup are essential for accurate pattern detection.

## Contributing
Contributions are welcome! Here’s how you can contribute:
1. Fork the repository.
2. Create a feature branch (e.g., `git checkout -b feature/YourFeature`).
3. Make your changes and commit them (e.g., `git commit -am 'Add new feature'`).
4. Push your branch and open a pull request detailing your changes.

Happy coding and happy pattern tracing!
