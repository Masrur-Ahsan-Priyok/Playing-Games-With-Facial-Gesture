def detect_landmarks(box, image):
    
    # For faster results convert the image to gray-scale
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Get the coordinates 
    (x1, y1, x2, y2) = box

    # Perform the detection
    shape = predictor(gray_scale, dlib.rectangle(x1, y1, x2, y2))
    
    # Get the numPy array containing the coordinates of the landmarks
    landmarks = shape_to_np(shape)
    
   # Draw the landmark points with circles 
    for (x, y) in landmarks:
        annotated_image = cv2.circle(image, (x, y),2, (0, 127, 255), -1)

    return annotated_image, landmarks
