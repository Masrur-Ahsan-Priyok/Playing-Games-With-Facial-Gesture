# Get the video feed from webcam
cap = cv2.VideoCapture(0)

# Set the window to a normal one so we can adjust it
cv2.namedWindow('Face proximity', cv2.WINDOW_NORMAL)

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
        
        # Check if face is closer than the defined threshold
        is_face_close,_ = face_proximity(box_coords, face_image, proximity_threshold = 325)
        
        # Display the mouth status
        cv2.putText(face_image,'Is Face Close: {}'.format(is_face_close),
                    (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 127, 255),2)

        
    # Display the frame
    cv2.imshow('Face proximity',face_image)
    
    # Break the loop if 'q' key pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and destroy the window
cap.release()
cv2.destroyAllWindows()
