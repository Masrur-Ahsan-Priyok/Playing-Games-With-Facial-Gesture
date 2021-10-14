# Get the video feed from webcam
cap = cv2.VideoCapture(0)

# Set the window to a normal one so we can adjust it
cv2.namedWindow('Mouth Status', cv2.WINDOW_NORMAL)

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
        
        # Get the landmarks for the face region in the frame
        landmark_image, landmarks = detect_landmarks(box_coords, frame)
        
        # Adjust the threshold and make sure it's working for you.
        mouth_status,_ = is_mouth_open(landmarks, ar_threshold = 0.6)
        
        # Display the mouth status
        cv2.putText(frame,'Is Mouth Open: {}'.format(mouth_status),
                    (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 127, 255),2)


    # Display the frame
    cv2.imshow('Mouth Status',frame)
    
    # Break the loop if 'q' key pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and destroy the window
cap.release()
cv2.destroyAllWindows()
