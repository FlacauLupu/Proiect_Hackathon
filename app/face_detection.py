import cv2
import mediapipe as mp

# Initialize mediapipe face detection
def detect_face(image_path):
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils

    # Load the image
    image = cv2.imread(image_path)

    # Convert the BGR image to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Initialize the face detection module
    with mp_face_detection.FaceDetection(min_detection_confidence=0.2) as face_detection:
        # Process the image
        results = face_detection.process(rgb_image)

        # Draw the face detection annotations on the image
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)

        # Display the image
        return image, results.detections
