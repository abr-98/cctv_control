import glob
import os
from check_faces import recognizer
from gtts import gTTS
def folder_check(unknown):
    folder=(glob.glob("/home/abhijit/atom_projects/reg_image/*"))
    flag=0
    textfile=open("/home/abhijit/atom_projects/files.txt","w")
    textfile.close()
    for i in folder:
        print(i)
        textfile=open("/home/abhijit/atom_projects/files.txt","a")
        textfile.write(i+"\n")
        textfile.close()
        files=(glob.glob(i+"/*"))
        for j in files:

            print(j)
            k=recognizer(j,unknown)
            if k==1:
                flag=1
                name=i[39:]
                person= name
                break
            if flag==1:
                break1
    if flag==0:
        name="unknown"

    if flag==1:
        mytext="Welcome "+name
        flag=1;
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("welcome.mp3")
        os.system("mpg321 welcome.mp3")
        os.remove("welcome.mp3")
        os.remove(unknown)
    else:
        mytext="Face recognition failed please report to office for more info.Thank You"
    	language = 'en'
    	myobj = gTTS(text=mytext, lang=language, slow=False)
    	myobj.save("welcome.mp3")
    	os.system("mpg321 welcome.mp3")
    	os.remove("welcome.mp3")
