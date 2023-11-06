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

# project module
import add_face


# engine = pyttsx3.init()
# engine.say("Welcome!")
# engine.say("Please browse through your options..")
# engine.runAndWait()


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


# to destroy screen
def del_sc1():
    sc1.destroy()

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

def adf():
    add_face.add_face()
    
def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="black")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
    titl.pack(fill=X)
    # image and title
    titl = tk.Label(
        ImageUI, text="Welcome HOME", bg="black", fg="green", font=("arial", 30),
    )
    titl.place(x=270, y=12)

    a = tk.Label(
        ImageUI,
        text="Register Your Face",
        bg="black",
        fg="yellow",
        bd=10,
        font=("arial", 24),
    )
    a.place(x=280, y=175)
    # image
    takeImg = tk.Button(
        ImageUI,
        text="Add Face",
        command=adf,
        bd=10,
        font=("times new roman", 18),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=280, y=250)

    


