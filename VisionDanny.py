import cv2
cap = cv2.VideoCapture(0)
eye_detection = cv2.CascadeClassifier("/home/tyson/Downloads/haarcascade_eye.xml")


while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_detection.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=60, minSize=(30,30))
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)





    cv2.imshow('test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break