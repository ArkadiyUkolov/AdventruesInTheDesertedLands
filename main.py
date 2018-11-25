from Tkinter import *
import numpy as np
import tkFileDialog
import os

root=Tk()
root.title("The GAME")


unlinearity = np.array([2, 3])

text_to_show = ('Wecome traveller, to the World of The Red Communistic Moon!' +
                '\n\nThis world was created by the will of Six-And-A-Half!' +
                '\n\nOr so we think.' +
                '\n\nGood luck.')
#button1_text = 'A'
#button2_text = 'B'

textbox = 0
button1 = 0
button2 = 0
event_number = 1
delta = 0

photo = PhotoImage(file='images/1.pgm')

panelFrame = Frame(root, bg = 'white')
textFrame = Frame(root, bg = 'black')

panelFrame.pack(side = 'bottom', fill = 'both')
textFrame.pack(side = 'left', fill = 'both', expand = 1)



def linear():
    global event_number, unlinearity
    i = 0
    while i < np.size(unlinearity):
        if event_number == unlinearity[i]:
            return False
        i += 1
    return True

def create_button():
    global panelFrame, button1, button2
    
    button1 = Button(panelFrame, pady = 20)
    button1.configure(text='A', width = 10, font = 'Arial 30', command=button_clicked1)
    button1.pack(side = 'left')

    button2 = Button(panelFrame, pady = 20)
    button2.configure(text='B', width = 10, font = 'Arial 30')

    print(linear())
    if linear():
        button2.configure(command=button_clicked1)
    else:
        button2.configure(command=button_clicked2)

    button2.pack(side = 'right')

def create_text():
    global textFrame, text_to_show, textbox, event_number, photo
    
    if os.path.isfile('images/{0}.pgm'.format(event_number)) == True:
        photo = PhotoImage(file = 'images/{0}.pgm'.format(event_number))
    
    textbox = Label(textFrame, text = text_to_show)
    textbox.configure(image = photo, anchor = 'w', compound = 'left', justify = 'left',
                      fg = 'white', bg = 'black', font=('Verdand', 20, "bold"), wraplength = 500)
    textbox.grid(row = 0)




def button_clicked1():
    global button1, button2, event_number, textbox, delta
    event_change()

    textbox.destroy()
    button1.destroy()
    button2.destroy()
    
    create_button()
    create_text()
    print(event_number, delta)

    if linear() == False:
       delta += 1
       event_number += delta
    else:
       event_number += 1


def button_clicked2():
    global button1, button2, event_number, textbox, delta
    event_change()

    textbox.destroy()
    button1.destroy()
    button2.destroy()
    
    create_button()
    create_text()
    
    if linear() == False:
       delta += 2
       event_number += delta
    else:
       event_number += 1



def event_change():
    global event_number, text_to_show, button1_text, button2_text
    text_to_show = loadtext(event_number)
#    button1_text = loadbuttons(event_number, 1)
#    button2_text = loadbuttons(event_number, 2)

def loadtext(event):
    f = open("story/{0}.txt".format(event),"r")
    string = f.read()
    return string

#def loadbuttons(event, number):
#    f = open("button{0}/{1}.txt".format(number, event),"r")
#    string = f.read()
#    f.close()
#    return string

create_button()
create_text()
root.mainloop()
