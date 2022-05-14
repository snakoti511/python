import cv2
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
  success, img = cap.read()
  data, qrPattern, success = detector.detectAndDecode(img)
  if qrPattern is not None:
    if data:
        cv2.putText(img,data,(10,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(	0, 255, 0),1 )
        print("QR Code detected, data:", data)
  cv2.imshow("img", img)
  
  if cv2.waitKey(1) == ord("q"):
    break
cap.release()
cv2.destroyAllWindows()
