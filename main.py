import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
import os
from turtle import clear
import typing
import PIL
from PIL import Image, ImageTk

from click import option
import yarl

window = Tk()
window.title("F451 Game")
window.configure(width = 800, height = 600)
window.configure(bg = "black") 

var = tk.IntVar()

#Functions
#Loading screen
def new_screen():

    start_button.destroy()
    close_button.destroy()
    info.destroy()

    start_button1.place(x = 150, y = 170, relwidth = 0.6, relheight = 0.5)


#Start screen
def new_screen2():
    start_button1.destroy()
    text2.place(x = 90, y = 170, relwidth = 0.8, relheight = 0.4)
    time.sleep(1)
    typing_text("You (Montag) come home from work, \n and see a mysterious girl.", text2)
    next_button1.place(x = 270, y = 450, relwidth = 0.36, relheight = 0.1)

#Third screen
def new_screen3():
    next_button1.destroy()
    typing_text("You decide to approach \nand talk to this new girl.", text2)
    time.sleep(1)
    typing_text("???: \"Do you mind if I walk back with you?\n I'm Clarisse McCellan.\"", text2)
    option_button1.place(x = 200, y = 450, relwidth = 0.25, relheight = 0.1)
    option_button2.place(x = 400, y = 450, relwidth = 0.25, relheight = 0.1)

#First Scene
def scene_1():
    option_button2.destroy()
    option_button1.destroy()
    time.sleep(0.5)
    typing_text("You: \"Sure\"", text2)
    time.sleep(0.5)
    typing_text("As you walk home with Clarisse, \nshe engages with a \ncontinuous stream of dialogue.", text2)
    next_button2_placing()
    typing_text("Clarisse: \"Have you read any of the \nbooks that you burned?\"", text2)
    next_button2_placing()
    typing_text("You: \"That's against the law!\"", text2) 
    next_button2_placing()
    typing_text("Clarisse: \"Oh, of course. Weren't firemen supposed to \nprevent fire from happening instead \nof burning fires themselves?\"", text2)
    next_button2_placing()
    typing_text("You: \"How ridiculous!\"", text2)
    time.sleep(0.75)
    typing_text("As you reach the doorstep, \nshe asks one decisive question.", text2)
    next_button2_placing()
    typing_text("Clarisse: \"Are you happy?\"", text2)
    time.sleep(2.9)
    typing_text("The grin vanishes from your face as your \ninsides churn at the simple thought.\n Your only words are silence, \nand unable to speak, Clarisse walks back the other way. \nYou stare at your home, \nnot looking so warm anymore.", text2)
    next_button2.configure(command = scene_2)
    next_button2_placing()

#Second scene
def scene_2():
    next_button2.configure(command = clear_text2)
    invis_button(next_button2)
    typing_text("You are burning books, cover after cover, \nas per your usual firemen routine.", text2)
    time.sleep(1.4)
    typing_text("The siren rings, \nbuzzing through the fire department. \nThere is a particularly hostile \nindividual in the vicinity.", text2)
    time.sleep(1.7)
    typing_text("Arriving at the scene, \nyour fellow firemen pour gallons of kerosene, \nencompassing the suspected house drenched.", text2)
    time.sleep(1.7)
    typing_text("Gazing at the suspect, \nyou spot a thin match peeking out \nof the suspected woman's hand, \nas she spouts heretic language.", text2)
    time.sleep(1.8)
    typing_text("You: \"Match!\"", text2)
    next_button2_placing()
    typing_text("Your co-workers frantically flee the scene, \nleaving you and the seemingly crazed woman.", text2)
    time.sleep(1.8)
    typing_text("You hesitate, \nnot able to shed the sympathetic feelings \nyou have for the woman's fate, \neven if it may be self-incurred. \nYou are left with two options. \nStay and convince her to evacuate, or RUN.", text2)
    option_button3.place(x = 200, y = 450, relwidth = 0.25, relheight = 0.1)
    option_button4.place(x = 400, y = 450, relwidth = 0.25, relheight = 0.1)

    


#Bomb ending
def bomb_ending():
    option_button2.destroy()
    option_button1.destroy()
    text2.place(x = 100, y = 100, relwidth = 0.7, relheight = 0.7)
    typing_text("You slowly walk away, \navoiding Clarisse's disappointing demeanor.", text2)
    time.sleep(1.3)
    typing_text("A life of nothingness, the life you live is a lie, \nand you intend to stay in the broken euphoria. \nYou can only wonder what this Clarisse girl was on about. \nLiving the life of a mere facade, \nyour life ends moments after bombs rain down, \nkilling off the lifeles corpse of yours.", text2)
    time.sleep(1)
    text2.configure(text = "")
    text2.destroy()
    # insert = f"{os.getcwd()}\Death_by_bomb_ending.png"
    # filename = tk.PhotoImage(file = insert)
    # background_label = Label(window, image = filename)
    # background_label.place(x=0, y=0, relwidth=1, relheight=1)
    death_by_atomic_bomb_ending_label.place(relwidth = 1, relheight = 1)

#Burning House Ending
def burning_house_ending():
    option_button3.destroy()
    option_button4.destroy()
    typing_text("As you stare into her grave eyes, \nshe says one final, decisive line.", text2)
    time.sleep(1)
    typing_text("Heretic Woman: \"Go on. There is no use saving a lunatic like me.\"", text2)
    time.sleep(1.5)
    text2.place(x = 100, y = 100, relwidth = 0.7, relheight = 0.7)
    typing_text("The matchstick ignites, \nwith your last moments of your life flashing with red and orange, \nthe colors of a phoenix. First, combustion. \nThen followed fire. What was left was your ashes. \nYou ran out of time.", text2)
    time.sleep(2)
    text2.configure(text = "")
    text2.destroy()
    #insert = f'{os.getcwd()}\Death_by_fire_pic.png'
    #burning_house.place(relwidth=1, relheight=1)
    death_by_fire_label.place(relwidth = 1, relheight = 1)

#First book
def the_First_Book():
    option_button3.destroy()
    option_button4.destroy()
    typing_text("You evaluate that your life is prioritized \nover her impossible to redempt life, \nand breathlessly evacuate out of the house. \nBriefly succeeding your grand escape, \ndrastic hellfire enrages the house.", text2)
    time.sleep(1)
    typing_text("Looking upon the remains of the house, \nyou notice a corner poking out of where \nthe garden should have been, \nlest the fire's ferocity didn't engulf the house.", text2)
    time.sleep(1.4)
    typing_text("You, while the others seem to be distracted, \nunearth the ground to uncover a book, \nnamely, the Bible.", text2)
    time.sleep(1.7)
    next_button2_placing()
    typing_text("Fascinated by this artifact of a book, \nyou take the book out of sheer curiosity, \neven if it drastically contrasts fireman conduct.", text2)
    time.sleep(1.7)
    typing_text("You contemplate where the perfect spot \nto conceal the books would be. \nThe three choices you have \nconjured are the bed, garden, and the sofa.", text2)
    time.sleep(1.8)
    bed_button.place(x = 100, y = 450, relwidth = 0.2, relheight = 0.1)
    garden_button.place(x = 300, y = 450, relwidth = 0.2, relheight = 0.1)
    couch_button.place(x = 500, y = 450, relwidth = 0.2, relheight = 0.1)
    
#Bed Hiding spot  
def bed():
    bed_button.destroy()
    garden_button.destroy()
    couch_button.destroy()  
    typing_text("In fear that this prized book be snatched away, \nyou hide the book under the pillows, \nproviding easy access and proximity for safeguarding.", text2)
    time.sleep(1.4)
    next_button2_placing()
    typing_text("You manage to narrowly get away with hiding the book, \ndespite a few close calls from Mildred and \nfuture visits from Captain Beatty himself.", text2)
    next_button2.configure(command = dialogue_with_Beatty)
    next_button2_placing()
    
#Garden Hiding spot
def garden():
    bed_button.destroy()
    garden_button.destroy()
    couch_button.destroy() 
    typing_text("To pay homage to where you initially found the book, \nfeeling inspired, you also embed the book into the garden. \nAfter all, no one would be insane to search a book there! Right?", text2)
    time.sleep(1.4)
    next_button2_placing()
    typing_text("You manage to narrowly get away with hiding the book, \ndespite a few close calls from Mildred and \nfuture visits from Captain Beatty himself.", text2)
    next_button2.configure(command = dialogue_with_Beatty)
    next_button2_placing()
    
    
#Couch Hiding spot
def couch():
    bed_button.destroy()
    garden_button.destroy()
    couch_button.destroy() 
    typing_text("Normally, the crevices of the sofa may have \nseemed like a proficient hiding spot for any book. \nHowever, much to your dismay, your wife, \nMildred, parks herself on the couch \nto watch the wall. \nShe is discomforted when sitting down. \nWhen she looks down, \nshe is revealed to a corner of the book, \nand to much of your horror, \nshe reports you to the fire department.", text2)
    time.sleep(2)
    next_button2_placing()
    typing_text("The next day, \nyou find yourself behind bars, \nsitting in death row, \npolitely waiting for your eventual demise…", text2)
    next_button2_placing()
    text2.destroy()
    #add_Background("jailed_ending_pic.png")
    death_by_mildred_label.place(relwidth = 1, relheight = 1)
    
#First dialogue with Beatty
def dialogue_with_Beatty():
    next_button2.configure(command = clear_text2)
    invis_button(next_button2)
    typing_text("After reading the Bible, \nyou go to sleep, \nin hopes for the refreshment of a new day to come.", text2)
    time.sleep(2)
    typing_text("Morning is apparent, \nand waking up doesn't change anything. \nYou don't remember work as appealing as it you remembered it to be. \nYou call in sick in hopes to mingle \nyour hands with this new book.", text2)
    time.sleep(2)
    typing_text("However, after a mere hour, \nyou sense a firm knock on the door vibrating throughout your house. \nGlimpsing through the door, \nyou encounter a wild Captain Beatty, \nawaiting on your doorstep.", text2)
    time.sleep(2)
    typing_text("After welcoming your superior inside cautiously, \nBeatty prepares to speak.", text2)
    time.sleep(2)
    typing_text("Captain Beatty: \"Just thought I'd come back and \nsee how the sick man is.\"", text2)
    time.sleep(2)
    next_button2_placing()
    typing_text("Captain Beatty: \"Let me get straight to the point. \nI've seen it all. Long story short: \nyou have 24 hours to return the book, \nlest you end up like that Clarisse girl.\"", text2)
    time.sleep(2)
    typing_text("You: \"What do you mean?\"", text2)
    time.sleep(2)
    typing_text("Captain Beatty: \"Clarisse is dead. Dead either way; \nif the car didn't get to her first, \nwe would've became her demise— like we always are.\"", text2)
    time.sleep(2)
    typing_text("Captain Beatty: \"Once again, \nI'll give you 24 hours sharp to burn that book into ashes. \nThe day of, \nand you'll see what it feels like to be the one on fire.\"", text2)
    time.sleep(2)
    next_button2.configure(command = meeting_Faber)
    next_button2_placing() 
    
#Meeting Faber
def meeting_Faber():
    next_button2.configure(command = clear_text2)
    invis_button(next_button2)
    typing_text("Following the departure of Captain Beatty, \nyou ponder on your next lead of information. \nIn the midst of your thoughts, \nyou recall an old man with a sleek, \nblack suit acting suspiciously secretive in a park.", text2)
    time.sleep(2)
    typing_text("Upon further thinking, \nyou realize that he shoved a rectangular object \nup his coat during your brief encounter with him. \nWhen approaching him, he is paranoid, \nbut reluctantly introduces himself as Faber and \nhands a thin strip of paper, fleeing from the area.", text2)
    time.sleep(1)
    locate_whereabouts_button.place(x = 200, y = 450, relwidth = 0.25, relheight = 0.1)
    follow_Beatty_button.place(x = 400, y = 450, relwidth = 0.25, relheight = 0.1)
    
#Brainwash Ending
def follow_Beatty():
    locate_whereabouts_button.destroy()
    follow_Beatty_button.destroy()
    typing_text("Deciding Captain Beatty knows best, \nyou follow his orders and return to your monotonous life of a fireman, \nbut you can't seem to stop feeling sensations of guilt. \nNevertheless, you are back to your fireman duties.", text2)
    clear_text2()
    time.sleep(1)
    #add_Background("brainwash_ending_pic.png")
    brainwash_ending_label.place(relwidth = 1, relheight = 1)    


def locate_whereabouts():
    locate_whereabouts_button.destroy()
    follow_Beatty_button.destroy()
    next_button2.configure(command = clear_text2)
    invis_button(next_button2)
    typing_text("Recalling from your old memories, \nyou read the address written on the slip of information. \nIn order to seek out the necessary answered, \nyou decide to venture out the given address, \nin order to interrogate Faber.", text2)
    next_button2_placing()
    typing_text("On a train ride, you intently memorize parts of the bible, \nhoping to retain content before the potency to be burnt to a crisp. \nMuch to Faber's dismay, you arrive at his house. \nReluctantly letting you in, \nhis cautiousness is replaced by awe with his sights glued to the Bible. \nHe asks where you found such a treasure, and taking advantage of this, \nyou request for aid. After a lengthy discourse, \nyou two seem to resonate.", text2)
    next_button2_placing()
    typing_text("When you pitch in your plan to overthrow society, \nFaber is incredulous, finding the idea insane. \nWith such a desperate measure, \nyou begin to rip the Bible apart, page after page. \nFaber, in a complete state of panic, submits to the plan, and \nprovides you a two-way communication device, advising you remotely. \nYour operations have started.", text2)
    next_button2.configure(command = dialogue_with_Mildred)
    next_button2_placing()
    
def dialogue_with_Mildred():
    next_button2.configure(command = clear_text2)
    invis_button(next_button2)
    typing_text("Arriving home, Mildred's incessant laughter \ncan be heard ripping through the hallway. \nHer laughter was bearable in the past, \nbut 'tis not the case now. \nHer echoing laughter haunts you, \namplifying your sickening thoughts.", text2)
    time.sleep(2)
    typing_text("You: \"When has anything mattered to \nyou other than those DAMN WALLS?\"", text2)
    next_button2_placing()
    typing_text("Mildred, not expecting your unwonted scream, \ndetaches her gaze at the walls, \nher nerves seemingly jumping out of her.", text2)
    time.sleep(2)
    typing_text("Mildred: \"What do you mean? \nThese are my relatives.\"", text2)
    time.sleep(2)
    typing_text("You: \"This is absurd! \nThey are not your relatives, I am! \nI am your husband, not the walls!\"", text2)
    next_button2_placing()
    typing_text("At this point, \nthe disdainful dispute could have gone for hours, \nif it were not for your active fireman duties.", text2)
    next_button2.configure(command = dialogue_with_Beatty2)
    next_button2_placing()
    
def dialogue_with_Beatty2():
    next_button2.configure(command = clear_text2)
    invis_button(next_button2)
    typing_text("Entering the fire station for your shift, \nyou are reminded of the approaching end of the \n24-hour grace period to submit the Bible.", text2)
    time.sleep(2)
    typing_text("Before you have a chance to address this, \nthe fire alarm rings as usual, \nbut you can't help but to feel uneasy \nabout this ominous alarm in particular.", text2)
    time.sleep(2)
    typing_text("Following your customary routines, \nyou lodge yourself onto the fire truck. \nAs the truck arrives closer to the destination, \nyou can't help but to question, \n\"Why have we stopped in front of my house?\"", text2)
    next_button2_placing()
    typing_text("In an onslaught of events, \nyou come to a final confrontation with Beatty in front of your home, \nroaring with fire dramatically. \nBeatty, gloating victoriously, looks down on you, \nrambling on increasingly verbose, frustrating phrases, \nfueling the rage residing in you.", text2)
    time.sleep(2)
    typing_text("Subsequently following the words of Beatty, \nyou pick up a flamethrower and lock your aim between Beatty's eyes. \nBeatty retorts with, \n\"Go ahead, you second-hand litterateur. Pull the trigger.\"\n You are left with desperate options and a flamethrower.", text2)
    time.sleep(0.5)
    spare_Beatty_button.place(x = 200, y = 450, relwidth = 0.25, relheight = 0.1)
    incinerate_Beatty_button.place(x = 400, y = 450, relwidth = 0.25, relheight = 0.1)

def death_by_Beatty_ending():
    spare_Beatty_button.destroy()
    incinerate_Beatty_button.destroy()
    typing_text("You cannot bring yourself to spare Beatty, \naffected by his silver tongue. \nYou found yourself at an ultimatum, \nand wimp out on your intended plans. \nFaber despairs through the radio device, \nwhile you condemn yourself to reluctancy, \nand drop dead before you feel astonishment. \nYour indecisiveness left Beatty to capitalize this opportunity.", text2)
    next_button2.configure(command = clear_text2)
    next_button2_placing()
    #add_Background("death_by_beatty_pic.png")
    death_by_beatty_label.place(relwidth = 1, relheight = 1) 

def incinerate_Beatty():
    spare_Beatty_button.destroy()
    incinerate_Beatty_button.destroy()
    next_button2.configure(command = clear_text2)
    invis_button(next_button2)
    typing_text("Channeling your bottled up rage, \nyou blind yourself from the ramifications and pull the trigger. \nBeatty writhes from the searing heat and reels on the ground. \nBeatty may be gone from the equation, \nbut your problems have only multiplied.", text2)
    next_button2_placing()
    typing_text("Staring down at the shriveled body of Beatty, \nyou can hear the Mechanical Hound's proximity.\n Acknowledging this, you bolt away at the spur of the moment. \nTraversing through streets, you seek for refuge.", text2)
    time.sleep(2)
    typing_text("You arrive at the only haven that occurs to you—- \nFaber's house. \nUpon arrival, he recognizes the dire situation you are in, \nand Faber decides to sacrifice himself and stay, \nknowing that he will only drag you behind. \nAs a final parting gift, he presents you his clothes to mask \nyour scent from the Mechanical Hound. \nYou run away, determined.", text2)
    time.sleep(2)
    typing_text("Off you ran, once again through the twisting narrow streets \nof the cities you once loved. \nWith whirling helicopters shining their headlight on your every move and police on par, \nyou continue to be frantically chased.", text2)
    next_button2.configure(command = join_living_libraries)
    next_button2_placing()
    
def join_living_libraries():
    next_button2.configure(command = clear_text2)
    invis_button(next_button2)
    typing_text("Through a stroke of luck, \nyou manage to best the pursuing forces, \nmasking your trail by diving into a river, \nand letting the flow drift you out of the city.", text2)
    time.sleep(2)
    typing_text("You were unconscious, and woke up near the shore. \nA group of men are visible in the distance, \nencircling a campfire. \nYou cautiously approach them, \nand they notice you as well.", text2)
    next_button2_placing()
    typing_text("The men introduce themselves as the \n\"Living Libraries,\" with each to their own book to fully memorize, \nword for word.", text2)
    next_button2_placing()
    typing_text("They offer you to join their forces, \nto set out on a mission to preserve knowledge. \nIn the distance, you and the men could hear \nbombs from the war raining like hellfire, \ndiminishing the city into rubble. \nYou gladly accept the offer.",text2)
    next_button2_placing()
    typing_text("Walking into the ashes of civilization, \nyou aspire for the amelioration and \ngeneral betterment of the grave society you were exiled from. \nThe ruined landscape streaks across your eyes, \nreflecting them with well-deserved tears.",  text2)
    time.sleep(7)
    ending_label.place(x = 90, y = 170, relwidth = 0.8, relheight = 0.4)
    
    
    


#Creates a typing effect
#TODO time.sleep should be (0.05)
def typing_text(text1, textBox):
    textBox.configure(text = "")
    first_text = text1
    text = ""
    for i in range(len(first_text)):
        text += first_text[i]
        textBox.configure(text = text)
        window.update()
        time.sleep(0.05)

def next_button2_placing():
    next_button2.place(x = 260, y = 450, relwidth = 0.3, relheight= 0.2)
    next_button2.wait_variable(var)

#Adding backgrounds (Don't use the function)

def add_Background(fileName):

    #path = f"{os.getcwd()}\Test.png"
    insert = f'{os.getcwd()}\{fileName}'
    print(insert)
    filename = tk.PhotoImage(file = insert)
    print(fileName)
    print(filename)
    background_label = Label(window, image = filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Makes the button invisible and continues the game
def clear_text2():
    text2.configure(text = "")
    var.set(1)
    invis_button(next_button2)
    var.set(0)
#Creating all the labels



#Creating all the buttons

start_button1 = tk.Button(window, text = "Click to start as Montag", width = 100, height = 20, bg = "green", fg = "white", font = "Arial 14", command = new_screen2)

next_button1 = tk.Button(window, text = "Click to keep going", width = 200, height = 20, bg = "green", fg = "red", font = "Arial 14", command = new_screen3)
next_button2 = tk.Button(window, text = "Click to keep going", width = 200, height = 20, bg = "orange", fg = "blue", font = "Arial 14", command = clear_text2)

option_button1 = tk.Button(window, text = "Sure", width = 100, height = 20, bg = "green", fg = "red", font = "Arial 14", command = scene_1)
option_button2 = tk.Button(window, text = "No, I'm good", width = 100, height = 20, bg = "green", fg = "red", font = "Arial 14", command = bomb_ending)
option_button3 = tk.Button(window, text = "Run", width = 100, height = 20, bg = "green", fg = "red", font = "Arial 14", command = the_First_Book)
option_button4 = tk.Button(window, text = "Stay", width = 100, height = 20, bg = "green", fg = "red", font = "Arial 14", command = burning_house_ending)

bed_button = tk.Button(window, text = "Bed", width = 100, height = 20, bg = "green", fg = "red", font = "Arial 14", command = bed)
garden_button = tk.Button(window, text = "Garden", width = 100, height = 20, bg = "green", fg = "red", font = "Arial 14", command = garden)
couch_button = tk.Button(window, text = "Couch", width = 100, height = 20, bg = "green", fg = "red", font = "Arial 14", command = couch)

locate_whereabouts_button = tk.Button(window, text = "Locate Faber", width = 100, height = 20, bg = "green", fg = "red", font = "Arial 14", command = locate_whereabouts)
follow_Beatty_button = tk.Button(window, text = "Follow Beatty", width = 100, height = 20, bg = "green", fg = "red", font = "Arial 14", command = follow_Beatty)

spare_Beatty_button = tk.Button(window, text = "Spare Beatty", width = 100, height = 20, bg = "green", fg = "red", font = "Arial 14", command = death_by_Beatty_ending)
incinerate_Beatty_button = tk.Button(window, text = "Incinerate Beatty", width = 100, height = 20, bg = "green", fg = "red", font = "Arial 14", command = incinerate_Beatty)

#Sets an image which can be configured
def set_Background_Image(image_path):
    background_label = Label(window, image_path)
    background_label.place(x=200, y=0, relwidth=1, relheight=1)

#useless
def change():
    if window.cget("bg") == "black":
        window.configure(bg = "white")
    else:
        window.configure(bg = "black")

#Makes the button invisible
def invis_button(button):
    button.place(x = 0, y = 0, relwidth = 0, relheight = 0)

#Buttons
start_button = tk.Button(window, text = "Start", width = 10, height = 5, bg = "green", fg = "white", font = "Arial 14", command = new_screen)
start_button.place(x = 140, y = 75,  relwidth = 0.2, relheight = 0.2)

close_button = tk.Button(window, text = "Close", width = 10, height = 5, bg = "red", fg = "white", font = "Arial 14", command = window.destroy)
close_button.place(x = 540, y = 75, relwidth = 0.2, relheight = 0.2)

info = Label(window, text = "This project was created by Derrick Ahn, Andy Le, and Shawn Gazin. (Period 4 & 6)", width = 200, height = 50, bg = "white", fg = "black", font = "Arial 14")
info.place(x = 0, y = 200, relwidth = 1, relheight = 0.3)

text2 = Label(window, width = 200, height = 50, bg = "white", fg = "black", font = "Arial 14", padx = 10, pady = 10)
ending_label = Label(window, text = "Credits: \nCoding- \nShawn Gazin (4th Period) \nPlot \n- Derrick Ahn (6th Period) \n- Andy Le (6th Period)", width = 200, height = 50, bg = "black", fg = "white", font = "Arial 14", padx = 10, pady = 10)


death_by_atomic_bomb_ending_label = Label(window, text = "Death by atomic bomb", width = 200, height = 50, bg = "red", fg = "black", font = "Arial 20", padx = 10, pady = 10)
death_by_fire_label = Label(window, text = "Death by fire", width = 200, height = 50, bg = "red", fg = "black", font = "Arial 20", padx = 10, pady = 10)
death_by_mildred_label = Label(window, text = "Death by Mildred", width = 200, height = 50, bg = "red", fg = "black", font = "Arial 20", padx = 10, pady = 10)
brainwash_ending_label = Label(window, text = "Brainwash ending", width = 200, height = 50, bg = "red", fg = "black", font = "Arial 20", padx = 10, pady = 10)
death_by_beatty_label = Label(window, text = "Death by Beatty", width = 200, height = 50, bg = "red", fg = "black", font = "Arial 20", padx = 10, pady = 10)

#burning_house = Label(window, image = ImageTk.PhotoImage(Image.open(f'{os.getcwd()}\Death_by_fire_pic.png')), width = 800, height = 600)
#window.attributes("-fullscreen", True)

# set_Background_Image("C:\Users\shawn\Documents\Code Projects\English F451 Final\test.png")



window.mainloop()