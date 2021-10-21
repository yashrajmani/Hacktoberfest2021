import cv2

#Capturing video using webcam 
video = cv2.VideoCapture(0)

#initializing trained data
face = cv2.CascadeClassifier('face.xml')
smile = cv2.CascadeClassifier('smile.xml')

while True:
    #obtaining the frame from video
    success,frame = video.read()

    #coonverting the frame to grayscale
    gframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Feeding the frame to algorithm for detection
    detectFace = face.detectMultiScale(gframe)

    for (x,y,w,h) in detectFace:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
        #find all simle within the face
        detectSmile = smile.detectMultiScale(gframe,scaleFactor = 1.7, minNeighbors=35) #remember these values!

        #writing the simle when smiling
        if len(detectSmile)>0:
            cv2.putText(frame,"HEHEHEHE.....!",(x,y+h+40),fontScale=1,fontFace=cv2.FONT_HERSHEY_COMPLEX,color=(255,255,255))

    cv2.imshow("Smile Detector",frame)
    key = cv2.waitKey(1)
    if(key == 81 or key == 281):
        break
video.release()
print("code completed!")