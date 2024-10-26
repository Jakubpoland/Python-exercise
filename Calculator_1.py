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



from tkinter import *  #Import biblioteki


root = Tk()
root.title("Kalkulator") #Nazwanie okienka
root.geometry("700x500")

main = Entry(root, width=40, borderwidth=5, font=('Arial', 18), justify='right')  #Ustalenie wyglądu okienka wpisu
main.grid(row=0, column=0, columnspan=4, padx=10, pady=10) 

history_entry = Entry(root, width=40, font=('Arial', 18), justify='right') #Ustalenie wyglądu histori
history_entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

history_display = Text(root, width=30, height=20, font=('Arial', 12), state=NORMAL) #Ustalenie wyglądu histori po prawej stronie
history_display.grid(row=0, column=4, rowspan=6, padx=10, pady=10)

def button_click(number): #Funkcja odpowiadająca za wpisywanie liczb
    cur = main.get()
    main.delete(0, END)
    main.insert(0, str(cur) + str(number))
    
def button_cl(): #Funkcja odpowiadająca za czyszczenie
    main.delete(0, END)
    main.delete(0, END)
    history_entry.delete(0, END)
    
def button_add():
    first_number = main.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    

def button_equal(): #Funkcja odpowiadająca za wynik 
    second_number = main.get()
    main.delete(0, END)
    main.insert(0, f_num + int(second_number))

def calculate():
    expression = main_entry.get().strip()
    result, infix_expression = rpn_to_infix_and_calculate(expression)
    if result is not None:
        # Wstawienie wyniku do głównego paska i infiksowego wyrażenia do drugiego
        main_entry.delete(0, END)
        main_entry.insert(END, str(result))
        
        history_entry.delete(0, END)
        history_entry.insert(END, infix_expression)
        
        # Dodanie do historii po prawej stronie
        history_display.insert(END, f"ONP: {expression}\nInfiks: {infix_expression} = {result}\n\n")



# Tworzenie przycisków numerycznych i operacyjnych
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
    ('0', 5, 0), ('C', 5, 1), ('=', 5, 2), ('/', 5, 3)
]

# Dodawanie przycisków do okna
for (text, row, col) in buttons:
    if text == '=':
        button = Button(root, text=text, width=5, height=2, font=('Arial', 18),
                           command=calculate)
    elif text == 'C':
        button = Button(root, text=text, width=5, height=2, font=('Arial', 18),
                           command=button_cl)
    else:
        button = Button(root, text=text, width=5, height=2, font=('Arial', 18),
                           command=lambda t=text: add_to_expression(t))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()



