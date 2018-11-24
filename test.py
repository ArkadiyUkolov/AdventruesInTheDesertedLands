from Tkinter import *
import tkFileDialog

def Event_Change():
    global event_number, text_to_show, button1_text, button2_text
    text_to_show = loadtext(event_number)
    button1_text = loadbuttons(event_number, 1)
    button2_text = loadbuttons(event_number, 2)

def loadtext(event):
    f = open("text{0}.txt".format(event),"r")
    string = f.read()
    return string

def loadbuttons(event, number):
    f = open("button{0}_{1}.txt".format(number, event),"r")
    string = f.read()
    f.close()
    return string


text_to_show = ' '
button1_text = ' '
button2_text = ' '
event_number = input(int())

Event_Change()
print(event_number, text_to_show, button1_text, button2_text)
