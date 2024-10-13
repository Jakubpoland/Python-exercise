import tkinter as tk
from tkinter import messagebox


# Funkcja obliczająca wynik wyrażenia w ONP i tłumacząca na notację infiksową
def rpn_to_infix_and_calculate(expression):
    stack = []
    infix_stack = []
    
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }

    tokens = expression.split()
    
    for token in tokens:
        if token in operators:
            try:
                b = stack.pop()
                a = stack.pop()
                result = operators[token](a, b)
                stack.append(result)
                
                infix_b = infix_stack.pop()
                infix_a = infix_stack.pop()
                infix_stack.append(f"({infix_a} {token} {infix_b})")
            except IndexError:
                messagebox.showerror("Błąd", "Za mało argumentów dla operatora!")
                return None, None
        else:
            try:
                value = float(token)
                stack.append(value)
                infix_stack.append(str(token))
            except ValueError:
                messagebox.showerror("Błąd", "Nieprawidłowe dane wejściowe!")
                return None, None

    if len(stack) == 1:
        return stack.pop(), infix_stack.pop()
    else:
        messagebox.showerror("Błąd", "Nieprawidłowe wyrażenie ONP!")
        return None, None


# Funkcja do obliczania wyniku i wyświetlania go w polach tekstowych oraz dodawania do historii
def calculate():
    expression = main_entry.get().strip()
    result, infix_expression = rpn_to_infix_and_calculate(expression)
    if result is not None:
        # Wstawienie wyniku do głównego paska i infiksowego wyrażenia do drugiego
        main_entry.delete(0, tk.END)
        main_entry.insert(tk.END, str(result))
        
        history_entry.delete(0, tk.END)
        history_entry.insert(tk.END, infix_expression)
        
        # Dodanie do historii po prawej stronie
        history_display.insert(tk.END, f"ONP: {expression}\nInfiks: {infix_expression} = {result}\n\n")


# Funkcja dodająca kliknięte liczby i operatory do głównego pola tekstowego
def add_to_expression(value):
    current_text = main_entry.get()
    main_entry.delete(0, tk.END)
    main_entry.insert(tk.END, current_text + value + ' ')


# Funkcja czyszcząca pole tekstowe
def clear_expression():
    main_entry.delete(0, tk.END)
    history_entry.delete(0, tk.END)


# Tworzenie okna głównego aplikacji
root = tk.Tk()
root.title("Kalkulator ONP")
root.geometry("700x500")

# Tworzenie pasków edycyjnych (głównego i historii)
main_entry = tk.Entry(root, width=40, font=('Arial', 18), justify='right')
main_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

history_entry = tk.Entry(root, width=40, font=('Arial', 18), justify='right')
history_entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Tworzenie pola tekstowego do wyświetlania historii po prawej stronie
history_display = tk.Text(root, width=30, height=20, font=('Arial', 12), state=tk.NORMAL)
history_display.grid(row=0, column=4, rowspan=6, padx=10, pady=10)

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
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                           command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                           command=clear_expression)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                           command=lambda t=text: add_to_expression(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Uruchomienie aplikacji
root.mainloop()
