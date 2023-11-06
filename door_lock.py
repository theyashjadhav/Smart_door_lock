import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3
from PIL import Image, ImageTk

import home


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


haarcasecade_path = "C:\\Users\\Shubhangi Jadhav\\att\\ams\\ams\\haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "C:\\Users\\Shubhangi Jadhav\\att\\ams\\ams\\TrainingImageLabel\\Trainner.yml"
)
trainimage_path = "C:\\Users\\Shubhangi Jadhav\\att\\ams\\ams\\TrainingImage"
studentdetail_path = (
    "C:\\Users\\Shubhangi Jadhav\\att\\ams\\ams\\StudentDetails\\studentdetails.csv"
)
attendance_path = "C:\\Users\\Shubhangi Jadhav\\att\\ams\\ams\\Attendance"


def FillAttendance():
    now = time.time()
    future = now + 20
    try:
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(trainimagelabel_path)
   
        facecasCade = cv2.CascadeClassifier(haarcasecade_path)
        df = pd.read_csv(studentdetail_path)
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        flag = True
        while flag:
            ___, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = facecasCade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                global Id

                Id, conf = recognizer.predict(gray[y : y + h, x : x + w])
                print(Id)
                if conf > 80:
                    flag = False
                    print(conf)
                    global tt
                    tt = str(Id) 
                    cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 4)
                    cv2.putText(
                        im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4
                    )
                else:
                    Id = "Unknown"
                    tt = str(Id)
                    cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                    cv2.putText(
                        im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4
                    )
            if time.time() > future:
                break

            cv2.imshow("Filling Attendance...", im)
            key = cv2.waitKey(30) & 0xFF
            if key == 27:
                break

        if flag:
            m = "locked"
            cam.release()
            cv2.destroyAllWindows()
        else:
            m ="UNlocked"
            cam.release()
            cv2.destroyAllWindows()
            home.TakeImageUI()
    except:
        cv2.destroyAllWindows()


window = Tk()
window.title("Face recognizer")
window.geometry("1280x720")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background="black")


# to destroy screen
def del_sc1():
    sc1.destroy()


# error message for name and no
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="black")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="yellow",
        bg="black",
        font=("times", 20, " bold "),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="yellow",
        bg="black",
        width=9,
        height=1,
        activebackground="Red",
        font=("times", 20, " bold "),
    ).place(x=110, y=50)


def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True


logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 47))
logo1 = ImageTk.PhotoImage(logo)

titl = Label(window, bg="black", relief="ridge", bd=10, font=("arial", 35))
titl.pack(fill="x")

l1 = Label(window, image=logo1, bg="black")
l1.place(x=470, y=10)

titl = tk.Label(
    window, text="Smart Lock!!", bg="black", fg="green", font=("arial", 27),
)
titl.place(x=525, y=12)

a = tk.Label(
    window,
    text="Welcome to Smart Door lock Based\n on Face Recognition  System",
    bg="black",
    fg="yellow",
    bd=10,
    font=("arial", 35),
)
a.pack()

r = tk.Button(
    window,
    text="Unlock",
    command=FillAttendance,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=520, y=520)

# Notifica = tk.Label(
#         text="Attendance filled Successfully",
#         bg="yellow",
#         fg="black",
#         width=33,
#         height=2,
#         font=("times", 15, "bold"),
#     )






window.mainloop()
