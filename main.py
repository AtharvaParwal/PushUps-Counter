import cv2
import mediapipe as md

md_drawing=md.solutions.drawing_utils
md_drawing_styles=md.solutions.drawing_styles
md_pose=md.solutions.pose

count=0

position=None

cap=cv2.VideoCapture(0)

with md_pose.Pose(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as pose:
    while cap.isOpened():
        success, image=cap.read()
        if not success:
            print("empty camera")
            break

        image=cv2.cvtColor(cv2.flip(image,1), cv2.COLOR_BGR2RGB)
        result=pose.process(image)
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        imlist=[]

        if result.pose_landmarks:
            md_drawing.draw_landmarks(
                image,result.pose_landmarks, md_pose.POSE_CONNECTIONS)
            for id, im in enumerate(result.pose_landmarks.landmark):
                h,w,_=image.shape
                X,Y=int(im.x *w), int(im.y *h)
                imlist.append([id,X,Y])


        if len(imlist)!=0: 
            # if (imlist[12][2] and imlist[11][2] >= imlist[14][2] and imlist[13][2]):
            #     position="down"
            # if ((imlist[12][2] and imlist[11][2] <= imlist[14][2] and imlist[13][2]) and position=="down"):
            #     position="up"
            #     count+=1
            #     print(count)

            if ((imlist[12][2] - imlist[14][2])>=15 and (imlist[11][2] - imlist[13][2])>=15):
                position = "down"
            if ((imlist[12][2] - imlist[14][2])<=5 and (imlist[11][2] - imlist[13][2])<=5) and position == "down":
                position = "up"
                count +=1 
                print(count)

        cv2.imshow("Push-up counter", cv2.flip(image,1))
        key=cv2.waitKey(1)
        if key==ord('q'):
            break

cap.release()



# import cv2
# import mediapipe as md

# # Initialize Mediapipe Pose model
# md_drawing = md.solutions.drawing_utils
# md_drawing_styles = md.solutions.drawing_styles
# md_pose = md.solutions.pose

# count = 0  # Push-up counter
# position = None  # Track up/down position

# cap = cv2.VideoCapture(0)

# with md_pose.Pose(
#     min_detection_confidence=0.7,
#     min_tracking_confidence=0.7) as pose:
    
#     while cap.isOpened():
#         success, image = cap.read()
#         if not success:
#             print("Empty camera frame")
#             break

#         # Convert image format for processing
#         image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
#         result = pose.process(image)
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#         imlist = []

#         if result.pose_landmarks:
#             md_drawing.draw_landmarks(
#                 image, result.pose_landmarks, md_pose.POSE_CONNECTIONS)

#             for id, lm in enumerate(result.pose_landmarks.landmark):
#                 h, w, _ = image.shape
#                 X, Y = int(lm.x * w), int(lm.y * h)
#                 imlist.append([id, X, Y])

#         if len(imlist) != 0: 
#             # Get necessary body points (Shoulders, Wrists, and Hips)
#             right_shoulder = imlist[12][2]  # Right Shoulder (y-coordinate)
#             left_shoulder = imlist[11][2]   # Left Shoulder (y-coordinate)
#             right_wrist = imlist[16][2]     # Right Wrist (y-coordinate)
#             left_wrist = imlist[15][2]      # Left Wrist (y-coordinate)
#             right_hip = imlist[24][2]       # Right Hip (y-coordinate)
#             left_hip = imlist[23][2]        # Left Hip (y-coordinate)

#             # Push-up detection logic
#             if right_wrist >= right_shoulder and left_wrist >= left_shoulder:
#                 position = "down"

#             if right_wrist <= right_hip and left_wrist <= left_hip and position == "down":
#                 position = "up"
#                 count += 1
#                 print("Push-ups:", count)

#         # Display the image with landmarks
#         cv2.putText(image, f"Push-ups: {count}", (30, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
#         cv2.imshow("Push-up Counter", cv2.flip(image, 1))
#         key = cv2.waitKey(1)
#         if key == ord('q'):
#             break

# cap.release()
# cv2.destroyAllWindows()


        