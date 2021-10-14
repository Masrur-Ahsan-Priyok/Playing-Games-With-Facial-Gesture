# Path to the weights file
model_weights =  "model/res10_300x300_ssd_iter_140000_fp16.caffemodel"

# Path to the architecture file
model_arch = "model/deploy.prototxt.txt"

# Load the caffe model
net = cv2.dnn.readNetFromCaffe(model_arch, model_weights)
