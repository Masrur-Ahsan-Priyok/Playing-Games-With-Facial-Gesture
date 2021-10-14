def face_detector(image, threshold =0.7):
    
    # Get the height,width of the image
    h, w = image.shape[:2]

    # Apply mean subtraction, and create 4D blob from image
    blob = cv2.dnn.blobFromImage(image, 1.0,(300, 300), (104.0, 117.0, 123.0))
    
    # Set the new input value for the network
    net.setInput(blob)
    
    # Run forward pass on the input to compute output
    faces = net.forward()
    
    # Get the confidence value for all detected faces
    prediction_scores = faces[:,:,:,2]
    
    # Get the index of the prediction with highest confidence 
    i = np.argmax(prediction_scores)
    
    # Get the face with highest confidence 
    face = faces[0,0,i]
    
    # Extract the confidence
    confidence = face[2]
    
    # if confidence value is greater than the threshold
    if confidence > threshold:
        
        # The 4 values at indexes 3 to 6 are the top-left, bottom-right coordinates
        # scales to range 0-1.The original coordinates can be found by 
        # multiplying x,y values with the width,height of the image
        box = face[3:7] * np.array([w, h, w, h])
        
        # The coordinates are the pixel numbers relative to the top left
        # corner of the image therefore needs be quantized to int type
        (x1, y1, x2, y2) = box.astype("int")
        
        # Draw a bounding box around the face.
        annotated_frame = cv2.rectangle(image.copy(), (x1, y1), (x2, y2), (0, 0, 255), 2)
        output = (annotated_frame, (x1, y1, x2, y2), True, confidence)
    
    # Return the original frame if no face is detected with high confidence.
    else:
        output = (image,(),False, 0)
    
    
    return output
