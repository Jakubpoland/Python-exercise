#Stosuję angielskie nazwy dla funkcji i opisu wszystkich rzeczy
# 
# Tekst który się wyświetla jest po polsku, cały backend jest po polsku
# 
#
#A3. Kalkulator standardowy (jak Windows) w notacji ONP
#  (z tłumaczeniem z/do notacji nawiasowej)
#  a) dwa paski edycyjne (drugi pasek do operacji i historia)
#Xb) przyciski dla liczb X
#Xc) przyciski dla operacji arytmetycznych, itpX
#Xd) GUI TkinterX
#
#
#



from tkinter import * #Import biblioteki

root = Tk()
root.title("Kalkulator") #Nazwanie okienka

e = Entry(root, width=45, borderwidth=5)  #Ustalenie wyglądu okienka wpisu
e = Entry(root, width=45, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10) #Ustalenie wyglądy pola klawiszy

def button_click(number): #Funkcja odpowiadająca za wpisywanie liczb
    #e.delete(0, END)
    cur = e.get()
    e.delete(0, END)
    e.insert(0, str(cur) + str(number))
    
def button_cl(): #Funkcja odpowiadająca za czyszczenie
    e.delete(0, END)

def button():

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
#definicja przycisków liczb

button_addition  = Button(root, text="+", padx=40, pady=20)
button_subtraction = Button(root, text="-", padx=40, pady=20) 
button_multiplication = Button(root, text="*", padx=40, pady=20)
button_division = Button(root, text="/", padx=40, pady=20)
button_clear = Button(root, text="<-", padx=190, pady=20, command=button_cl)
button_equation = Button(root, text="=", padx=40, pady=20)
button_dot = Button(root, text=".", padx=40, pady=20)
#definicja przycisków akcji

#
#Zainicjowanie przycisków i ich wyglądu
#

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_division.grid(row=1, column=3)
#1 rząd przycisków

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiplication.grid(row=2, column=3)
#2 rząd przycisków

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtraction.grid(row=3, column=3)
#3 rząd przycisków

button_equation.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_dot.grid(row=4, column=2)
button_addition.grid(row=4, column=3)
#4 rząd przycisków



button_clear.grid(row=5, column=0, columnspan=4)

# 
# Rozmieszczenie ich na planszy  
# 

root.mainloop()



