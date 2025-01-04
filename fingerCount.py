import cv2
import os
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

# 手の画像が含まれているフォルダを指定して、ファイル名を取得する 
folderpath = "images"
img_list = os.listdir(folderpath)

# 手の画像を読み込む
finger_imgs = []
for file in img_list:
    image = cv2.imread(f'{folderpath}/{file}')
    finger_imgs.append(image)

detector = HandDetector(detectionCon=0.75)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        fingers = detector.fingersUp(hands[0])
        finger_num = fingers.count(1) # 伸びている指の数を数える
        h, w, _ = finger_imgs[finger_num].shape
        img[0:h, 0:w] = finger_imgs[finger_num]
        # 指の数を表示する
        cv2.rectangle(img, (20, 250), (170, 450), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, text=str(finger_num), org=(40, 410), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=6, color=(255, 0, 0), thickness=3)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()