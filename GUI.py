from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os
import time

root = Tk()
root.title("Sign Language Recogniser")
root.geometry('1100x700')

#Backgroung image
load = Image.open('C:\\Users\\Dev Prajapati\\PycharmProjects\\TEMiniProject\\images\\bg.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root,image=render)
img.place(x = 0,y=0)

#Button
img1 = PhotoImage(file = 'C:\\Users\\Dev Prajapati\\PycharmProjects\\TEMiniProject\\images\\button.png')


def btn1():
    messagebox.showinfo("NOTE", "-MAKE SURE CAMERA IS CONNECTED TO YOUR DEVICE\n"
                                "-YOU ARE SITTING IN A WELL LIT ENVIRONMENT\n"
                                "-YOUR BACKGROUND IS NOT NOISY\n")
    time.sleep(2)
    file1='framesextraction.py'
    os.system(file1)
    pass


b1 = Button(root,image = img1,command = btn1,bd=0, bg='#010101', activebackground='#010101')
b1.place(x=318, y=325)

img2 = PhotoImage(file='C:\\Users\\Dev Prajapati\\PycharmProjects\\TEMiniProject\\images\\Created-By-Dev-Prajapat.png')
l1 = Label(root, image = img2,bg='#010101', activebackground='#010101')
l1.place(x=10,y=650)

img3 = PhotoImage(file='C:\\Users\\Dev Prajapati\\PycharmProjects\\TEMiniProject\\images\\SIGN-LANGUAGE-RECOGNISER.png')
l2 = Label(root, image = img3, bg='#010101', activebackground='#010101')
l2.place(x=50,y=30)


root.mainloop()

