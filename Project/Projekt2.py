from tkinter import *

root = Tk()

def myClick():
    myLabel =  Label(root, text="Look i clicked")
    myLabel.pack()

myLabel = Label(root, text="Hello World")
myLabel.pack()
myButton = Button(root, text="click me", command=myClick, fg="blue", bg="orange")
myButton.pack()
root.mainloop()
