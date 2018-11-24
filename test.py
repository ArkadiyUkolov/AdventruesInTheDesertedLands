from Tkinter import *
import tkFileDialog


def create_Button():
    global panelFrame, button1_text, button2_text, button1, button2
    
    button1 = Button(panelFrame)
    button1.configure(text=button1_text, bg='gray', command=button_clicked)
    button1.pack(side = 'left')
    
    button2 = Button(panelFrame)
    button2.configure(text=button2_text, command=button_clicked)
    button2.pack(side = 'right')

def button_clicked():
    global button1, button2, button1_text, button2_text, event_number, textbox
    Event_Change()
    button1.destroy()
    button2.destroy()
    textbox.destroy()
    create_Text()
    create_Button()
    event_number += 1


def create_Text():
    global textFrame, text_to_show, textbox
    textbox = Text(textFrame, font='Arial 14', wrap='word')
    textbox.pack(side = 'left', fill = 'both', expand = 1)
    textbox.insert(END, text_to_show)


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


root=Tk()

textbox = 0
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
create_Text()
root.mainloop()
