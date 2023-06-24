

def detectGlasses(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, w, c = hsv_frame.shape
    cnt = 0
    if h != 0 and w != 0 and c != 0:
        for x in range(w):
            for y in range(h):
                if hsv_frame[y, x, 2] <= 100:
                    cnt += 1
    if cnt >= 5:
        return True
    return False


def getGlasses(frame):
    if frame is None: return False
    img = frame.copy()
    
    # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(img)
    x1, y1, x2, y2 = 0, 0, 0, 0
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(image=img, landmark_list=faceLms, connections=mpFaceMesh.FACEMESH_TESSELATION,
                                  connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())
        for id, lm in enumerate(faceLms.landmark):
            # print(lm)
            ih, iw, ic = img.shape
            if id == 55:
                x1, y1 = int(lm.x * iw), int(lm.y * ih)
            elif id == 412:
                x2, y2 = int(lm.x * iw), int(lm.y * ih)
    if x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:
        glasses_img = frame[y1:y2, x1:x2, :]
        # glasses_img = cv2.resize(glasses_img, (320, 240))
        if detectGlasses(glasses_img):
            # cv2.imshow("glasses_img", glasses_img)
            print("yessssssssssssssss")
            return True
        return False
