from app.face_detection import detect_face
import cv2

def test_face_detection():
    image_path = "images/face.jpg"
    image, detections = detect_face(image_path)

    # Save the image
    output_path = 'temp/test_output.jpg'
    cv2.imwrite(output_path, image)

    print(f"Faces detected: {len(detections)}")
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    test_face_detection()