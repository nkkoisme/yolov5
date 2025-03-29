import cv2
import torch
import numpy as np  # Required for np.squeeze()

# Initialize model (use absolute path for reliability)
model = torch.hub.load('ultralytics/yolov5', 'custom', 
                      path='runs/train/exp5/weights/best.pt')

# Set camera resolution (match your training size)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 416)  
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 416)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # Run detection
    results = model(frame)
    
    # Display
    cv2.imshow('YOLOv5 Webcam', np.squeeze(results.render()))
    
    # Exit on 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
