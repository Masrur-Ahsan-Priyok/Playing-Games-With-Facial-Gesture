# Get the video feed from webcam
cap = cv2.VideoCapture(0)

# Set the window to a normal one so we can adjust it
cv2.namedWindow('face Detection', cv2.WINDOW_NORMAL) 

while(True):
    
    # Read the frames
    ret, frame = cap.read()
    
    # Break if frame is not returned
    if not ret:
        break
        
    # Flip the frame
    frame = cv2.flip( frame, 1 )
    
    # Detect face in the frame
    annotated_frame, coords, status, conf = face_detector(frame)
    
    # Display the frame
    cv2.imshow('face Detection', annotated_frame)
    
    # Break the loop if 'q' key pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture and destroy the window
cap.release()
cv2.destroyAllWindows()
