import cv2
import numpy as np
import sys
import traceback

def process_frame(img):
    try:
        # Resize image for consistency
        img = cv2.resize(img, (512, 512))
    except Exception as e:
        print("Error resizing image:", e)
        traceback.print_exc()
        sys.exit(1)
    
    try:
        # Initialize ArUco detector
        parameters = cv2.aruco.DetectorParameters()
        aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
    except Exception as e:
        print("Error initializing ArUco parameters:", e)
        traceback.print_exc()
        sys.exit(1)
    
    try:
        # Detect markers in the image
        corners, ids, rejected = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)
    except AttributeError as e:
        print("Error: cv2.aruco does not have the attribute 'detectMarkers'.")
        print("Ensure opencv-contrib-python is installed.")
        sys.exit(1)
    except Exception as e:
        print("Error during marker detection:", e)
        traceback.print_exc()
        sys.exit(1)

    if ids is not None:
        print("Detected markers:", ids.flatten())
        cv2.aruco.drawDetectedMarkers(img, corners, ids)
        
        # Calculate marker positions
        marker_positions = [(np.mean(corner[0], axis=0)) for corner in corners]
        marker_positions = [pos for _, pos in sorted(zip(ids.flatten(), marker_positions))]
        
        # Generate movement instructions based on relative positions
        instructions = []
        for i in range(1, len(marker_positions)):
            prev_x, prev_y = marker_positions[i - 1]
            curr_x, curr_y = marker_positions[i]
            if abs(curr_x - prev_x) > abs(curr_y - prev_y):
                instructions.append("Move Right" if curr_x > prev_x else "Move Left")
            else:
                instructions.append("Move Down" if curr_y > prev_y else "Move Up")
        
        print("Instructions for the doodle car:", instructions)
    else:
        print("No markers detected.")
    
    cv2.imshow("Detected ArUco Markers", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    choice = input("Choose input source - 'I' for image, 'C' for camera: ").strip().upper()
    
    if choice == 'I':
        img_path = r"Doodlebot\images\aruco.jpg"
        try:
            img = cv2.imread(img_path)
            if img is None:
                raise FileNotFoundError(f"Image not found at {img_path}.")
        except Exception as e:
            print("Error loading image:", e)
            traceback.print_exc()
            sys.exit(1)
        process_frame(img)
    
    elif choice == 'C':
        try:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                raise Exception("Cannot open the camera.")
            print("Press 'q' to capture an image.")
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Camera frame capture failed. Retrying...")
                    continue
                cv2.imshow("Camera Feed - Press 'q' to capture", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    img = frame.copy()
                    break
            cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            print("Error accessing camera:", e)
            traceback.print_exc()
            sys.exit(1)
        
        process_frame(img)
    
    else:
        print("Invalid choice. Please choose 'I' or 'C'.")
        sys.exit(1)

if __name__ == "__main__":
    main()