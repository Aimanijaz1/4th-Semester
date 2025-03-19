import cv2
import os

# Load Haar Cascade model
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def analyze_face(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    if len(faces) == 0:
        return {"error": "No face detected"}

    x, y, w, h = faces[0]  # Only analyze the first detected face

    # Draw rectangle around face
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Create processed image directory
    processed_dir = os.path.join("static/uploads/processed")
    os.makedirs(processed_dir, exist_ok=True)

    # Save processed image
    processed_image_path = os.path.join(processed_dir, os.path.basename(image_path))
    cv2.imwrite(processed_image_path, image)

    # Extract face measurements
    forehead_length = h * 0.25  # Approximate forehead size
    eye_distance = w * 0.4      # Approximate eye distance

    # Simple personality prediction based on face ratio
    face_ratio = w / h
    personality = "Extrovert" if face_ratio > 0.9 else "Introvert"

    return {
        "face_width": w,
        "face_height": h,
        "forehead_length": round(forehead_length, 2),
        "eye_distance": round(eye_distance, 2),
        "personality": personality,
        "original_image": os.path.basename(image_path),
        "processed_image": os.path.basename(processed_image_path)
    }
