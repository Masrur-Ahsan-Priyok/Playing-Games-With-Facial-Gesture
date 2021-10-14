def face_proximity(box,image, proximity_threshold = 325):
    
    # Get the height and width of the face bounding box
    face_width =  box[2]-box[0]
    face_height = box[3]-box[1]
    
    # Draw rectangle to guide the user 
    # Calculate the angle of diagonal using face width, height 
    theta = np.arctan(face_height/face_width)
     
    # Use the angle to calculate height, width of the guide rectangle
    guide_height = np.sin(theta)*proximity_threshold
    guide_width  = np.cos(theta)*proximity_threshold
    
    # Calculate the mid-point of the guide rectangle/face bounding box
    mid_x,mid_y = (box[2]+box[0])/2 , (box[3]+box[1])/2
    
    # Calculate the coordinates of top-left and bottom-right corners
    guide_topleft = int(mid_x-(guide_width/2)), int(mid_y-(guide_height/2))
    guide_bottomright = int(mid_x +(guide_width/2)), int(mid_y + (guide_height/2))
    
    # Draw the guide rectangle
    cv2.rectangle(image, guide_topleft, guide_bottomright, (0, 255, 255), 2)
    
    # Calculate the diagonal distance of the bounding box
    diagonal = hypot(face_width, face_height)
    
    # Return True if distance greater than the threshold
    if diagonal > proximity_threshold:
        return True, diagonal
    else:
        return False, diagonal
