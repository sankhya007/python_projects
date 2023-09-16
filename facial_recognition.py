

#only to open the camra 


# import cv2

# def display_webcam():
#     cap = cv2.VideoCapture(0)

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to capture image")
#             break

#         cv2.imshow('Webcam Feed', frame)

#         # Break the loop when 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     display_webcam()








#facial recognition bot (only box)


import cv2
import mediapipe as mp

def detect_face_landmarks(image):
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils

    # Load MediaPipe Face Detection model
    face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.3)

    # Convert the image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Run face detection
    results = face_detection.process(image_rgb)

    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = image.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

    return image

if __name__ == "__main__":
    # Initialize webcam
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detect face landmarks
        frame_with_landmarks = detect_face_landmarks(frame)

        # Display the resulting frame
        cv2.imshow('Facial Landmark Detection', frame_with_landmarks)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close OpenCV window
    cap.release()
    cv2.destroyAllWindows()

