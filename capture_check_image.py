import cv2, time,sys
from PIL import Image
#from image_resize import img_resize
#from datetime import datetime
from gtts import gTTS
from face_detect_sec import read_image
import os
def capture(name,ctr):

    #os.makedirs("/home/abhijit/atom_projects/reg_image/"+name+")
  while True:
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

        delta_frame=cv2.absdiff(first_frame,gray)
        thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)


        cv2.imshow("Color Frame-ESC to close SPACE to capture",frame)

        key=cv2.waitKey(1)

        if key%256 == 27:
            #ESC
            print("closing")
            break
        elif  key%256 ==32:
            #SPACE
            img_ctr=str(img_counter)
            ct=str(ctr)
            img_name="/home/abhijit/atom_projects/reg_image/"+name+"/"+ct+".jpg".format(img_counter)
            cv2.imwrite(img_name,frame)
            if read_image(img_name)==1:

                mytext="capture "+ct+" successful.Thank you.Press escape to exit"
                flag=0
                #cv2.imwrite(img_name,frame)
                imk=Image.open(img_name)
                imk.load()
                language = 'en'
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("welcome.mp3")
                os.system("mpg321 welcome.mp3")
                os.remove("welcome.mp3")
                #imk.show()
                #print("written".format(img_name))
                img_counter+=1
                return img_name

            else:
                mytext="capture unsuccessful.Please try again adjusting light"
                flag=1;
                language = 'en'
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("welcome.mp3")
                os.system("mpg321 welcome.mp3")
                os.remove("welcome.mp3")
                os.remove(img_name)

    video.release()
    cv2.destroyAllWindows()
    #img_name="reg_image/frame_"+name+".jpg".format(img_counter)
    #img_resize(img_name)
    #print(img_ctr)
    if flag==0:
      break
#if  __name__=="__main__":
#    capture("abhijit",1)
