import cv2, time,sys
from gtts import gTTS
from capture_check_image import capture
import os
from subprocess import call

def create_set(name):
    os.makedirs("/home/abhijit/atom_projects/reg_image/"+name)
    count=15
    n1="/home/abhijit/atom_projects/reg_image/"+name
    #t1= int(round(time.time()))
    mytext="Starting camera creating data set.Please keep changing your position from camera and facial expression for better performance.Thank you"
    flag=1;
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")
    os.remove("welcome.mp3")
    #t=2
    #img_extension=capture(name,count)
    #count=count-1;
    while True:
        #t2= int(round(time.time()))
        if count==0:
            break


        img_extension=capture(name,count)
        count=count-1;

    mytext="Data set created thank you for cooperation"
    flag=1;
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")
    os.remove("welcome.mp3")
    exec_code=call("python3 /home/abhijit/atom_projects/face_lock/encode_face.py  --dataset reg_image --encodings encodings.pickle",shell=True)
    return n1

if __name__ == '__main__':
    create_set("Abhijit98")
