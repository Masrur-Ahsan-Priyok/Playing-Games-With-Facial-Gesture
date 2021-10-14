# Get the video feed from webcam
cap = cv2.VideoCapture(0)

# Set the window to a normal one so we can adjust it
cv2.namedWindow('Dino with OpenCV', cv2.WINDOW_NORMAL)

# By default each key press is followed by a 0.1 second pause
pyautogui.PAUSE = 0.0

# The fail-safe triggers an exception in case mouse
# is moved to corner of the screen
#pyautogui.FAILSAFE = False

while(True):
    
     # Read the frames
    ret, frame = cap.read()
    
    # Break if frame is not returned
    if not ret:
        break
        
    # Flip the frame
    frame = cv2.flip( frame, 1 )
    
    # Detect face in the frame
    face_image, box_coords, status, conf = face_detector(frame)
    
    if status:
        
        # Detect landmarks if a face is found
        landmark_image, landmarks = detect_landmarks(box_coords, frame)
        
        # Check if mouth is open
        is_open,_ = is_mouth_open(landmarks, ar_threshold)
        
        # If the mouth is open trigger space key Down event to jump
        if is_open:
            
            pyautogui.keyDown('space')
            mouth_status = 'Open'

        else:
            # Else the space key is Up
            pyautogui.keyUp('space')
            mouth_status = 'Closed'
        
        # Display the mouth status on the frame
        cv2.putText(frame,'Mouth: {}'.format(mouth_status),
                    (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 127, 255),2)
        
        # Check the proximity of the face
        is_closer,_  = face_proximity(box_coords, frame, proximity_threshold)
        
        # If face is closer press the down key
        if is_closer:
            pyautogui.keyDown('down')
            
        else:
            pyautogui.keyUp('down')
        
    # Display the frame
    cv2.imshow('Dino with OpenCV',frame)

    # Break the loop if 'q' key pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
