from Tkinter import *
import tkFileDialog

root=Tk()
root.title("The GAME")

textbox = 0
button1 = 0
button2 = 0
text_to_show = ('Wecome traveller, to the World of The Red Communistic Moon!' +
                '\n\nThis world was created by the will of Six-And-A-Half!' +
                '\n\nOr so we think.' +
                '\n\nGood luck.')
button1_text = 'Next'
button2_text = 'Next'
event_number = 1
delta = 0

photo = PhotoImage(file='images/1.pgm')

panelFrame = Frame(root, bg = 'white')
textFrame = Frame(root, bg = 'black')

panelFrame.pack(side = 'bottom', fill = 'both')
textFrame.pack(side = 'left', fill = 'both', expand = 1)


def create_button():
    global panelFrame, button1_text, button2_text, button1, button2, event_number
    
    button1 = Button(panelFrame, pady = 20)
    button1.configure(text=button1_text, font = 'Arial 30', command=button_clicked1)
    button1.pack(side = 'left')

    button2 = Button(panelFrame, pady = 20)
    button2.configure(text=button2_text, font = 'Arial 30')
    if event_number == 1:
        button2.configure(command=button_clicked1)
    else:
        button2.configure(command=button_clicked2)
    button2.pack(side = 'right')

def create_text():
    global textFrame, text_to_show, textbox, event_number, photo

    photo = PhotoImage(file = 'images/{0}.pgm'.format(event_number))
    
    textbox = Label(textFrame, text = text_to_show)
    textbox.configure(image = photo, anchor = 'nw', compound = 'left', fg = 'white', bg = 'black', font=('Verdand', 20, "bold"), wraplength = 500)
    textbox.grid(row = 0)




def button_clicked1():
    global button1, button2, event_number, textbox, delta
    event_change()

    button1.destroy()
    button2.destroy()
    textbox.destroy()
    
    create_text()
    create_button()
    
    delta += 1
    event_number += delta

def button_clicked2():
    global button1, button2, event_number, textbox, delta
    event_change()

    button1.destroy()
    button2.destroy()
    textbox.destroy()
    
    create_text()
    create_button()
    
    delta += 2
    event_number += delta




def event_change():
    global event_number, text_to_show, button1_text, button2_text
    text_to_show = loadtext(event_number)
    button1_text = loadbuttons(event_number, 1)
    button2_text = loadbuttons(event_number, 2)

def loadtext(event):
    f = open("story/{0}.txt".format(event),"r")
    string = f.read()
    return string

def loadbuttons(event, number):
    f = open("button{0}/{1}.txt".format(number, event),"r")
    string = f.read()
    f.close()
    return string



create_button()
create_text()
root.mainloop()
