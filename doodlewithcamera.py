import cv2
import numpy as np

# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 is the default camera

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Resize the frame
        frame = cv2.resize(frame, (512, 512))

        # Load the dictionary and detector parameters
        aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
        parameters = cv2.aruco.DetectorParameters()
        
        # Detect the markers
        corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
        
        if ids is not None:
            print("Detected markers are:", ids.flatten())
            # Draw the detected markers
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)
            
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
            
        # Display the frame
        cv2.imshow("Detected ArUco Markers", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()
