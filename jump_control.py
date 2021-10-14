def is_mouth_open(landmarks, ar_threshold = 0.7): 
    
    
    # Calculate the euclidean distance labelled as A,B,C
    A = hypot(landmarks[50][0] - landmarks[58][0], landmarks[50][1] - landmarks[58][1])
    B = hypot(landmarks[52][0] - landmarks[56][0], landmarks[52][1] - landmarks[56][1])
    C = hypot(landmarks[48][0] - landmarks[54][0], landmarks[48][1] - landmarks[54][1])
    
    # Calculate the mouth aspect ratio
    # The value of vertical distance A,B is averaged
    mouth_aspect_ratio = (A + B) / (2.0 * C)
    
    # Return True if the value is greater than the threshold
    if mouth_aspect_ratio > ar_threshold:
        return True, mouth_aspect_ratio
    else:
        return False, mouth_aspect_ratio
