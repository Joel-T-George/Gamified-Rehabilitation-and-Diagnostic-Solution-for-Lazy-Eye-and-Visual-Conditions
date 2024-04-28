import cv2 as cv
import numpy as np
import mediapipe as mp
import pyautogui
screen_w, screen_h = pyautogui.size()
mp_face_mesh = mp.solutions.face_mesh
LEFT_IRIS = [474,475,476,477]
RIGHT_IRIS =[469,470,471,472]
camera = cv.VideoCapture(0)
with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5
) as face_mesh:

    while True:

        ret, frame = camera.read()
        if not ret:
            break
        frame =cv.flip(frame,1)
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        img_h, img_w = frame.shape[:2]
        result = face_mesh.process(rgb_frame)
        
        if result.multi_face_landmarks:
            
            mesh_points = np.array([np.multiply([p.x,p.y],[img_w,img_h]).astype(int) for p in result.multi_face_landmarks[0].landmark])
           
            (l_cx, l_cy), l_radius = cv.minEnclosingCircle(mesh_points[LEFT_IRIS])
            (r_cx, r_cy), r_radius = cv.minEnclosingCircle(mesh_points[RIGHT_IRIS])
            center_left = np.array([l_cx,l_cy], dtype=np.int32)
            center_right = np.array([r_cx,r_cy], dtype=np.int32)
            midpoint_left = (l_cx, l_cy)
            midpoint_right = (r_cx, r_cy)
            cv.circle(frame, center_left, int(l_radius), (255,0,0),1,cv.LINE_AA)
            cv.circle(frame, center_right, int(r_radius), (255,0,0),1,cv.LINE_AA)
            cv.circle(frame, (int(midpoint_left[0]), int(midpoint_left[1])), 2, (0, 0, 255), -1)
            cv.circle(frame, (int(midpoint_right[0]), int(midpoint_right[1])), 2, (0, 0, 255), -1)

            #cv.circle(frame, mesh_points[159], 2, (255,255,255),1,cv.LINE_AA)
            #cv.circle(frame, mesh_points[145], 2, (255,255,255),1,cv.LINE_AA)
            #cv.circle(frame, mesh_points[362], 2, (255,255,255),1,cv.LINE_AA)
            #cv.circle(frame, mesh_points[263], 2, (255,255,255),1,cv.LINE_AA)
            screenX = (screen_w /img_w )* midpoint_left[0] 
            screenY = (screen_h / img_h )* midpoint_left[1] 
            pyautogui.moveTo(screenX, screenY)
            blink= [mesh_points[145],mesh_points[159]]

            if (blink[0][1]-blink[1][1]) <= 9:
                pyautogui.click()
                print("click")
                pyautogui.sleep(1)
            
            #print(mesh_points)
            #cv.polylines(frame, )
        cv.imshow('video', frame)
        key =cv.waitKey(1)
        if key == ord('a'):
            break
    camera.release()
    cv.destroyAllWindows()