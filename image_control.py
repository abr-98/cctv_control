import tkinter as tk
from tkinter import messagebox
import MySQLdb
import mysql.connector
from subprocess import call
import re
from create_file import create_set




def picture(name):
  conn= mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      db="face_lock"
  )
  mycursor = conn.cursor()
  img_extension=create_set(name)
  mycursor.execute('UPDATE user_data SET PHOTO_LINK= "%s" WHERE NAME = "%s"'%(img_extension,name))
  conn.commit()


def image_control(name):

  root =tk.Tk()
  root.geometry('400x300')
  root.title("Registration Form")

  tk.Button(root, text='Thank You ',width=20,bg='brown',fg='white',command=picture(name)).place(x=100,y=80)
  root.destroy()
  #root.mainloop()

#if __name__ == '__main__':
#    image_control("Abhijit Roy")
