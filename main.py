from Tkinter import *
import numpy as np
import tkFileDialog
import os

root=Tk()
root.title("The GAME")

text_to_show = ('THE GAME')

#button1_text = 'A'
#button2_text = 'B'

event_number = 0
textbox = 0
button1 = 0
button2 = 0

junctions = [
        ('story/exam/A/A'),
        ('story/exam/A/B'),
        ('story/exam/B/A'),
        ('story/exam/B/B')
    ]

end = [
        ('story/city/A/2.txt')
    ]

new_way = [
        ('story/city'),
        ('story/city'),
        ('story/city'),
        ('story/city')
    ]


way = 'story/exam'

photo = PhotoImage(file=(way + '/1.pgm'))

panelFrame = Frame(root, bg = 'white')
textFrame = Frame(root, bg = 'black')

panelFrame.pack(side = 'bottom', fill = 'both')
textFrame.pack(side = 'left', fill = 'both', expand = 1)



#def linear():
 #   global event_number, unlinearity
 #   i = 0
 #   while i < np.size(unlinearity):
 #       if event_number == unlinearity[i]:
 #           return False
 #       i += 1
 #   return True

def create_button():
    global panelFrame, button1, button2, event_number

    if event_number != 3:
        button1 = Button(panelFrame, pady = 20)
        button1.configure(text='NEXT', width = 20, font = 'Arial 30')
        button1.configure(command=button_linear)
        button1.pack(side = 'bottom')
       
    else:
       button1 = Button(panelFrame, pady = 20)
       button1.configure(text='Option A', width = 10, font = 'Arial 30')
       button1.configure(command=button_clicked1)

       button2 = Button(panelFrame, pady = 20)
       button2.configure(text='Option B', width = 10, font = 'Arial 30')
       button2.configure(command=button_clicked2)

       button1.pack(side = 'left')
       button2.pack(side = 'right')
       

def create_text():
    global textFrame, text_to_show, textbox, event_number, photo

    textbox = Label(textFrame, text = text_to_show)
    textbox.configure(anchor = 'w', compound = 'left', justify = 'left',
                      fg = 'white', bg = 'black', font=('Verdand', 20, "bold"), wraplength = 500)
    
    if os.path.isfile((way + "/{0}.pgm").format(event_number)) == True:
        photo = PhotoImage(file = (way + "/{0}.pgm").format(event_number))
        textbox.configure(image = photo)
    
    textbox.grid(row = 2)

    WAY_TEST = Label(textFrame, text = ((way + "/{0}.pgm").format(event_number)))
    WAY_TEST.grid(row = 0)




def button_linear():
    global button1, event_number, textbox
    
    textbox.destroy()
    button1.destroy()
    
    event_number += 1
    
    event_change()
    create_button()
    create_text()

def button_clicked1():
    global button1, button2, event_number, textbox
    
    textbox.destroy()
    button1.destroy()
    button2.destroy()

    story_way('A')
    event_change()
    create_button()
    create_text()


def button_clicked2():
    global button1, button2, event_number, textbox

    textbox.destroy()
    button1.destroy()
    button2.destroy()

    story_way('B')
    event_change()
    create_button()
    create_text()

def story_way(letter):
    global way, event_number, junctions, new_way
    event_number = 1
    
    way = way + '/' + letter

    i = 0
    while i < np.size(junctions):
        if way == junctions[i]:
            way = new_way[i]
        i += 1

def event_change():
    global text_to_show
    text_to_show = loadtext()

def loadtext():
    global way, event_number, button1

    i = 0
    while i < np.size(end):
        if ((way + "/{0}.txt").format(event_number)) == end[i]:
            button1.destroy()
            return 'NO ESCAPE'
        else:
            f = open((way + "/{0}.txt").format(event_number),"r")
            string = f.read()
            return string
        i += 1
        
create_button()
create_text()
root.mainloop()
