import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\Ayush\Desktop\Doodle\aruco.jpg")
img = cv2.resize(img, (512, 512))

if img is None:
    print("Image not found. Check the path.")
else:
    # Load the dictionary and detector parameters
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
    parameters = cv2.aruco.DetectorParameters()
    
    # Detect the markers
    corners, ids, rejected = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)
    
    if ids is not None:
        print("Detected markers are:", ids.flatten())
        # Draw the detected markers
        cv2.aruco.drawDetectedMarkers(img, corners, ids)
        
        # Calculate marker positions and movement instructions
        marker_positions = []
        for corner in corners:
            # Calculate the center of each marker
            cx, cy = np.mean(corner[0], axis=0)
            marker_positions.append((cx, cy))

        # Sort markers by detected ID order to follow the path
        marker_positions = [pos for _, pos in sorted(zip(ids.flatten(), marker_positions))]

        # Generate movement instructions for the doodle car
        instructions = []
        for i in range(1, len(marker_positions)):
            prev_x, prev_y = marker_positions[i - 1]
            curr_x, curr_y = marker_positions[i]
            
            # Determine movement based on relative positions
            if abs(curr_x - prev_x) > abs(curr_y - prev_y):
                if curr_x > prev_x:
                    instructions.append("Move Right")
                else:
                    instructions.append("Move Left")
            else:
                if curr_y > prev_y:
                    instructions.append("Move Down")
                else:
                    instructions.append("Move Up")
        
        print("Instructions for the doodle car:", instructions)
        
    else:
        print("No markers detected.")
        
    # Display the image
    cv2.imshow("Detected ArUco Markers", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
