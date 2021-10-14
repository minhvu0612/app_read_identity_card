import cv2
import sys


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


while 1:
	ret, frame = cap.read()
	if not ret:
		sys.exit()
	frame = cv2.resize(frame, dsize = (800, 700))
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	_, threshold = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
	img_binary = cv2.adaptiveThreshold(gray, 
                                       maxValue=255, 
                                       adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, 
                                       thresholdType=cv2.THRESH_BINARY,
                                       blockSize=15,
                                       C=8)
	cv2.imshow("frame",frame)
	cv2.imshow("threshold",threshold)
	cv2.imshow("adaptive", img_binary)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break