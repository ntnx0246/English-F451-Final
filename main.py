import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
import os

from click import option

window = Tk()
window.title("F451 Game")
window.configure(width = 800, height = 600)
window.configure(bg = "black") 



#Functions
def new_screen():

    start_button.destroy()
    close_button.destroy()
    info.destroy()

    start_button1.place(x = 150, y = 170, relwidth = 0.6, relheight = 0.5)


def new_screen2():
    start_button1.destroy()
    first_text = "You (Montag) come home from work, \n and see a mysterious girl."
    text = ""
    text2.place(x = 200, y = 100, relwidth = 0.5, relheight = 0.5)
    time.sleep(1)
    for i in range(len(first_text)):
        text += first_text[i]
        text2.configure(text = text)
        window.update()
        time.sleep(0.05)
    next_button1.place(x = 300, y = 450, relwidth = 0.25, relheight = 0.1)

def new_screen3():
    next_button1.destroy()
    first_text = "You decide to approach \nand talk to this new girl."
    text = ""
    for i in range(len(first_text)):
        text += first_text[i]
        text2.configure(text = text)
        window.update()
        time.sleep(0.05)
    time.sleep(1)
    text2.configure(text = "")
    first_text = "??? Do you mind if I walk back with you?\n I'm Clarisse McCellan."
    text = ""
    for i in range(len(first_text)):
        text += first_text[i]
        text2.configure(text = text)
        window.update()
        time.sleep(0.05)
    option_button1.place(x = 200, y = 450, relwidth = 0.25, relheight = 0.1)
    option_button2.place(x = 400, y = 450, relwidth = 0.25, relheight = 0.1)

def option_1():
    option_button2.destroy()
    option_button1.destroy()
    time.sleep(0.5)
    text2.configure(text = "")
    first_text = "Sure"
    text = ""
    for i in range(len(first_text)):
        text += first_text[i]
        text2.configure(text = text)
        window.update()
        time.sleep(0.05)
    

def option_2():
    option_button2.destroy()
    option_button1.destroy()
    typing_text("You slowly walk away, \navoiding Clarisse's disappointing demeanor.", text2)
    text2.configure(text = "")
    typing_text("A life of nothingness, The life you live is a lie, \nand you intend to stay in the broken euphoria. \nYou can only wonder what this Clarisse girl was on about. \nLiving the life of a mere facade, \nyour life ends moments after bombs rain down, \nkilling off the lifeles corpse of yours.", text2)
    time.sleep(1)
    text2.configure(text = "")
    text2.destroy()
    atomic_bomb_ending_label.place(relwidth = 1, relheight = 1)


def typing_text(text1, textBox):
    first_text = text1
    text = ""
    for i in range(len(first_text)):
        text += first_text[i]
        textBox.configure(text = text)
        window.update()
        time.sleep(0.05)


#Adding backgrounds (Don't use the function)

def add_Background(fileName):

    #path = f"{os.getcwd()}\Test.png"
    insert = f"{os.getcwd()}\{fileName}"
    filename = PhotoImage(file = insert)
    background_label = Label(window, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Creating all the labels



#Creating all the buttons

start_button1 = tk.Button(window, text = "Click to start as Montag", width = 100, height = 20, bg = "green", fg = "white", font = "Arial 14", command = new_screen2)

next_button1 = tk.Button(window, text = "Click to keep going", width = 100, height = 20, bg = "green", fg = "red", font = "Arial 14", command = new_screen3)

option_button1 = tk.Button(window, text = "Sure", width = 100, height = 20, bg = "green", fg = "red", font = "Arial 14", command = option_1)
option_button2 = tk.Button(window, text = "No, I'm good", width = 100, height = 20, bg = "green", fg = "red", font = "Arial 14", command = option_2)

def set_Background_Image(image_path):
    background_label = Label(window, image_path)
    background_label.place(x=200, y=0, relwidth=1, relheight=1)


def change():
    if window.cget("bg") == "black":
        window.configure(bg = "white")
    else:
        window.configure(bg = "black")


#Buttons
start_button = tk.Button(window, text = "Start", width = 10, height = 5, bg = "green", fg = "white", font = "Arial 14", command = new_screen)
start_button.place(x = 140, y = 0,  relwidth = 0.2, relheight = 0.2)

close_button = tk.Button(window, text = "Close", width = 10, height = 5, bg = "red", fg = "white", font = "Arial 14", command = window.destroy)
close_button.place(x = 540, y = 0, relwidth = 0.2, relheight = 0.2)

info = Label(window, text = "This project was created by Derrick Ahn, Andy Lee, and Shawn Gazin. (Period 4 & 6)", width = 200, height = 50, bg = "white", fg = "black", font = "Arial 14")
info.place(x = 0, y = 200, relwidth = 1, relheight = 0.3)

text2 = Label(window, width = 200, height = 50, bg = "white", fg = "black", font = "Arial 14", padx = 10, pady = 10)

atomic_bomb_ending_label = Label(window, text = "Death by atomic bomb", width = 200, height = 50, bg = "red", fg = "black", font = "Arial 20", padx = 10, pady = 10)
#window.attributes("-fullscreen", True)



window.mainloop()