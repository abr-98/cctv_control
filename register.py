import tkinter as tk
from tkinter import messagebox
import MySQLdb
import mysql.connector
from subprocess import call
import re
from image_control import image_control
#from capture_check_image import capture
#from PIL import Image,ImageTk
root =tk.Tk()
root.geometry('500x500')
root.title("Registration Form")

Fullname=tk.StringVar()
name1=""
Email=tk.StringVar()
email=""
Permission=tk.StringVar()
permit=""

def isvalidemail(email):
    if len(email) > 7:
        if re.match("^.+@(\[?)\[a-zA-Z0-9-.\]+.(\[a-zA-Z\]\{2,3\}|\[0-9\]\{1,3\})(\]?)$", email) != None:
            return True
    return False
def database():
   conn= mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="face_lock"
   )
   mycursor = conn.cursor()

   name1=Fullname.get()
      # print(name1)
   if name1=="":
        messagebox.showerror(
                "Input NOT valid.",
                "Please try again and enter a valid input."
            )
        root.destroy()
        exec_code=call("python3 /home/abhijit/face_lock/atom_projects/register.py",shell=True)
   query="""SELECT * FROM user_data WHERE NAME='%s'"""%(name1)
   mycursor.execute(query)
   dup=mycursor.fetchall()
   i=mycursor.rowcount
   if i!=0:
        messagebox.showerror(
                "User exists.",
                "Please try again and enter a new email."
            )
        root.destroy()
        exec_code=call("python3 /home/abhijit/atom_projects/face_lock/register.py",shell=True)
   permit=Permission.get()
       # print(name1)
   if permit=="":
         messagebox.showerror(
                 "Input NOT valid.",
                 "Please try again and enter a valid input."
             )
         root.destroy()
         exec_code=call("python3 /home/abhijit/atom_projects/face_lock/register.py",shell=True)


   email=Email.get()
        #print(email)
   if email=="":
        messagebox.showerror(
                "Input NOT valid.",
                "Please try again and enter a valid input."
            )
        root.destroy()
        exec_code=call("python3 /home/abhijit/atom_projects/face_lock/register.py",shell=True)

   query="""SELECT * FROM user_data WHERE EMAIL='%s'"""%(email)
   mycursor.execute(query)
   dup=mycursor.fetchall()
   i=mycursor.rowcount
   if i!=0:
       messagebox.showerror(
               "Email exists.",
               "Please try again and enter a new email."
           )
       root.destroy()
   if isvalidemail(email):
       messagebox.showerror(
       
               "Invalid Mail.",
               "Please try again and enter a new email."
           )
       root.destroy()
       exec_code=call("python3 /home/abhijit/atom_projects/face_lock/register.py",shell=True)
  # conn = sqlite3.connect('Form.db')
   #with conn:
    #  cursor=conn.cursor()
   mycursor.execute('INSERT INTO user_data (NAME,EMAIL,PERMIT) VALUES("%s","%s","%s")'%(name1,email,permit))
   conn.commit()
   root.destroy()
   image_control(name1)
   #exec_code=call("python3 /home/abhijit/atom_projects/launch_window.py",shell=True)

label_0 = tk.Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = tk.Label(root, text="User Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 =tk.Entry(root,textvariable=Fullname)
entry_1.place(x=240,y=130)

label_2 =tk. Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 =tk.Entry(root,textvariable=Email)
entry_2.place(x=240,y=180)

label_3 =tk. Label(root, text="Permission",width=20,font=("bold", 10))
label_3.place(x=68,y=230)

entry_3 =tk.Entry(root,textvariable=Permission)
entry_3.place(x=240,y=230)


#tk.Button(root, text='Take Image',width=20,bg='brown',fg='white',command=take_image).place(x=180,y=280)
#root.destroy()
#image_control(name1)
#label_4.place(x=180,y=280)


tk.Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=300)


root.mainloop()
