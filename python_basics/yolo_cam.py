from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8s.pt")

# Open laptop webcam
cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    if not ret:
        break

    # Run YOLO detection
    results = model(frame)

    # Draw results on frame
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("YOLO Object Detection", annotated_frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()