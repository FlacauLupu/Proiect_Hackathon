import cv2
import face_recognition
import numpy as np
import json
import os

# File to store known faces
KNOWN_FACES_FILE = "employees/known_faces.json"

# Load known faces from JSON
def load_known_faces():
    if os.path.exists(KNOWN_FACES_FILE):
        with open(KNOWN_FACES_FILE, "r") as file:
            return json.load(file)
    return {}

# Save new face encoding to JSON
def save_face_encoding(name, encoding):
    known_faces[name] = encoding.tolist()  # Convert numpy array to list
    with open(KNOWN_FACES_FILE, "w") as file:
        json.dump(known_faces, file)

# Compare face encodings
def compare_faces(known_encodings, encoding_to_check, tolerance=0.6):
    for name, known_encoding in known_encodings.items():
        distance = np.linalg.norm(encoding_to_check - np.array(known_encoding))
        if distance < tolerance:
            return name
    return "Unauthorized"

# Main detection and recognition loop
def detect_and_recognize_faces():
    global known_faces
    known_faces = load_known_faces()

    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert frame to RGB for face_recognition
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect face locations and encodings
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), encoding in zip(face_locations, face_encodings):
            name = compare_faces(known_faces, encoding)

            # Draw a box around the face
            color = (0, 255, 0) if name != "Unauthorized" else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        # Display the frame
        cv2.imshow("Face Recognition", frame)

        # Save new face encoding with 's' key
        key = cv2.waitKey(1) & 0xFF
        if key == ord("s"):
            if(len(face_locations)>1):
                select = int(input("Select face to save (input number): "))
            else:
                select = 1
            name = input("Enter name for this face: ").strip()
            if name:
                save_face_encoding(name, face_encodings[len(face_locations)-select])
                print(f"Saved face for {name}")

        # Exit on 'q' key
        elif key == ord("q"):
            print("Exiting...")
            break   

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_and_recognize_faces()
