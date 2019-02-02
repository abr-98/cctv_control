import cv2,time
from PIL import Image
import time
import datetime
from gtts import gTTS
from face_detect_sec import read_image
import os
from subprocess import call
def capture():
    t1= int(round(time.time()))
    now_time=datetime.datetime.now().time().strftime("%X")
    now_time_str=str(now_time)
    first_frame=None
    status_list=[None,None]
    #times=[]
    #df=pandas.DataFrame(columns=["Start","End"])
    img_counter=0
    video=cv2.VideoCapture(0)

    while True:
        check, frame = video.read()
        status=0
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray=cv2.GaussianBlur(gray,(21,21),0)

        if first_frame is None:
            first_frame=gray
            continue

        t2= int(round(time.time()))


        delta_frame=cv2.absdiff(first_frame,gray)
        thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)
        img_name="/home/abhijit/atom_projects/unreg_image/frame_rec"+now_time_str".jpg".format(img_counter)
        if t2-t1==2:
            cv2.imwrite(img_name,frame)

            if read_image(img_name)==1:
                mytext="face detected.Processing.Please wait"
                flag=1;
                language = 'en'
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("welcome.mp3")
                os.system("mpg321 welcome.mp3")
                os.remove("welcome.mp3")
                exec_code=call("python3 recognizer.py --encodings encodings.pickle --image"+ img_name)

                #os.remove(img_name)
                break;
            else:
                mytext="face not detected.Please ensure proper light and your face is not covered"
                flag=1;
                language = 'en'
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("welcome.mp3")
                os.system("mpg321 welcome.mp3")
                os.remove("welcome.mp3")
                os.remove(img_name)
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    capture()
