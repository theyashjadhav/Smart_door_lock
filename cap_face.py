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
import tkinter.ttk as tkk
import tkinter.font as font

haarcasecade_path = "C:\\Users\\Shubhangi Jadhav\\att\\ams\\ams\\haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "C:\\Users\\Shubhangi Jadhav\\att\\ams\\ams\\TrainingImageLabel\\Trainner.yml"
)
trainimage_path = "C:\\Users\\Shubhangi Jadhav\\att\\ams\\ams\\TrainingImage"
studentdetail_path = (
    "C:\\Users\\Shubhangi Jadhav\\att\\ams\\ams\\StudentDetails\\studentdetails.csv"
)
attendance_path = "C:\\Users\\Shubhangi Jadhav\\att\\ams\\ams\\Attendance"
# for choose subject and fill attendance
def subjectChoose():
       
    def FillAttendance():
        now = time.time()
        future = now + 20
        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            try:
                recognizer.read(trainimagelabel_path)
            except:
                e = "Model not found,please train model"
                Notifica.configure(
                    text=e,
                    bg="black",
                    fg="yellow",
                    width=33,
                    font=("times", 15, "bold"),
                )
                Notifica.place(x=20, y=250)
            facecasCade = cv2.CascadeClassifier(haarcasecade_path)
            df = pd.read_csv(studentdetail_path)
            cam = cv2.VideoCapture(0)
            font = cv2.FONT_HERSHEY_SIMPLEX
            while True:
                ___, im = cam.read()
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                faces = facecasCade.detectMultiScale(gray, 1.2, 5)
                for (x, y, w, h) in faces:
                    global Id

                    Id, conf = recognizer.predict(gray[y : y + h, x : x + w])
                    if conf > 30:
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

  
            m = "Attendance Filled Successfully of "
            Notifica.configure(
                text=m,
                bg="black",
                fg="yellow",
                width=33,
                relief=RIDGE,
                bd=5,
                font=("times", 15, "bold"),
            )
            

            Notifica.place(x=20, y=250)

            cam.release()
            cv2.destroyAllWindows()
        except:
            cv2.destroyAllWindows()

    ###windo is frame for subject chooser
    subject = Tk()
    # windo.iconbitmap("AMS.ico")
    subject.title("Subject...")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="black")
    # subject_logo = Image.open("UI_Image/0004.png")
    # subject_logo = subject_logo.resize((50, 47), Image.ANTIALIAS)
    # subject_logo1 = ImageTk.PhotoImage(subject_logo)
    titl = tk.Label(subject, bg="black", relief=RIDGE, bd=10, font=("arial", 30))
    titl.pack(fill=X)
    # l1 = tk.Label(subject, image=subject_logo1, bg="black",)
    # l1.place(x=100, y=10)


    Notifica = tk.Label(
        subject,
        text="Attendance filled Successfully",
        bg="yellow",
        fg="black",
        width=33,
        height=2,
        font=("times", 15, "bold"),
    )



    fill_a = tk.Button(
        subject,
        text="Fill Attendance",
        command=FillAttendance,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=RIDGE,
    )
    fill_a.place(x=195, y=170)
    subject.mainloop()
