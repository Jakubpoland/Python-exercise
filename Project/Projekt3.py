from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Wpisz dane")

def myClick():
    myLabel =  Label(root, text=e.get())
    myLabel.pack()


myButton = Button(root, text="click me", command=myClick, fg="blue", bg="orange")
myButton.pack()
root.mainloop()
