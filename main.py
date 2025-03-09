import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe Pose model
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Counter & Position
count = 0  
position = None  

# Open webcam
cap = cv2.VideoCapture(0)

with mp_pose.Pose(
    static_image_mode=False,  
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as pose:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Empty camera frame")
            break

        # Convert image format for processing
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = pose.process(image_rgb)

        imlist = []

        if result.pose_landmarks:
            mp_drawing.draw_landmarks(image, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            for id, lm in enumerate(result.pose_landmarks.landmark):
                h, w, _ = image.shape
                X, Y = int(lm.x * w), int(lm.y * h)
                imlist.append([id, X, Y])

        if len(imlist) != 0:
            # Extract key points for push-up detection
            right_shoulder = imlist[12][2]  
            left_shoulder = imlist[11][2]   
            right_elbow = imlist[14][2]
            left_elbow = imlist[13][2]
            right_hip = imlist[24][2]       
            left_hip = imlist[23][2]        

            # Push-up detection based on elbow and shoulder height
            if ((right_shoulder - right_elbow) >= 15 and (left_shoulder - left_elbow) >= 15):
                position = "down"

            if ((right_shoulder - right_elbow) <= 5 and (left_shoulder - left_elbow) <= 5) and position == "down":
                position = "up"
                count += 1 
                print(f"Push-ups: {count}")

        # Display push-up count
        cv2.putText(image, f"Push-ups: {count}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow("Push-up Counter", image)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
