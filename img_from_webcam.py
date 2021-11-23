import cv2

cam = cv2.VideoCapture(0)
#cv2.namedWindow("Human Detection Frame")
img_counter = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to get the frame")
        break
    cv2.imshow("Human Detection Frame",frame)
    if 0xFF == ord('q'):
        wait = cv2.waitKey(1)
        break


cam.release()
cam.destroyAllWindows()