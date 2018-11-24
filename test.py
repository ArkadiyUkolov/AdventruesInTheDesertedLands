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

def create_Button():
    global panelFrame, button1_text, button2_text, button1, button2
    
    button1 = Button(panelFrame)
    button1.configure(text=button1_text, command=button_clicked)
    button1.pack(side = 'left')
    
    button2 = Button(panelFrame)
    button2.configure(text=button2_text, command=button_clicked)
    button2.pack(side = 'right')

def button_clicked():
    global button1, button2, button1_text, button2_text
    Event_Change()
    button1.destroy()
    button2.destroy()
    create_Button()

root=Tk()

button1 = 0
button2 = 0
text_to_show = ' '
button1_text = ' '
button2_text = ' '
event_number = 1

panelFrame = Frame(root, height = 100, bg = 'gray')
textFrame = Frame(root, height = 340, width = 600)

panelFrame.pack(side = 'bottom', fill = 'x')
textFrame.pack(side = 'top', fill = 'both', expand = 1)

create_Button()
root.mainloop()
