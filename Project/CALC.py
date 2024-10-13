"""
import tkinter as tk

# Funkcja, która dodaje cyfrę lub operator do wyświetlacza
def kliknij(przycisk):
    obecna_wartosc = pole_wyniku.get()
    pole_wyniku.delete(0, tk.END)
    pole_wyniku.insert(tk.END, obecna_wartosc + str(przycisk))

# Funkcja, która czyści wyświetlacz
def wyczysc():
    pole_wyniku.delete(0, tk.END)

# Funkcja, która wykonuje obliczenie
def oblicz():
    wyrazenie = pole_wyniku.get()
    try:
        wynik = eval(wyrazenie)  # eval wykonuje operacje matematyczne
        pole_wyniku.delete(0, tk.END)
        pole_wyniku.insert(tk.END, str(wynik))
    except Exception as e:
        pole_wyniku.delete(0, tk.END)
        pole_wyniku.insert(tk.END, "Błąd")

# Tworzenie głównego okna
okno = tk.Tk()
okno.title("Kalkulator")

# Pole do wyświetlania wyników
pole_wyniku = tk.Entry(okno, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
pole_wyniku.grid(row=0, column=0, columnspan=4)

# Przycisk i jego przypisanie do odpowiednich funkcji
przyciski = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Tworzenie przycisków
for (przycisk, rzad, kolumna) in przyciski:
    if przycisk == '=':
        tk.Button(okno, text=przycisk, width=5, height=2, font=('Arial', 18),
                  command=oblicz).grid(row=rzad, column=kolumna)
    else:
        tk.Button(okno, text=przycisk, width=5, height=2, font=('Arial', 18),
                  command=lambda przycisk=przycisk: kliknij(przycisk)).grid(row=rzad, column=kolumna)

# Przycisk czyszczenia
tk.Button(okno, text='C', width=5, height=2, font=('Arial', 18),
          command=wyczysc).grid(row=4, column=2)

# Uruchomienie głównej pętli aplikacji
okno.mainloop()
"""

import tkinter as tk

# Funkcja do obliczania wyrażeń w notacji ONP
def oblicz_onp(wyrazenie):
    stos = []
    for element in wyrazenie.split():
        if element.isdigit():  # Jeśli jest to liczba, dodaj do stosu
            stos.append(int(element))
        else:  # Jeśli jest to operator, pobierz dwie ostatnie liczby i wykonaj operację
            b = stos.pop()
            a = stos.pop()
            if element == '+':
                stos.append(a + b)
            elif element == '-':
                stos.append(a - b)
            elif element == '*':
                stos.append(a * b)
            elif element == '/':
                stos.append(a / b)
    return stos.pop()  # Zwróć wynik (powinno pozostać jedno rozwiązanie na stosie)

# Funkcja do wywoływania obliczeń, zależnie od trybu (standardowy lub ONP)
def oblicz():
    wyrazenie = pole_wyniku.get()
    try:
        if tryb_onp.get():  # Jeśli zaznaczony tryb ONP
            wynik = oblicz_onp(wyrazenie)
        else:  # Tryb standardowy
            wynik = eval(wyrazenie)  # eval wykonuje operacje matematyczne
        pole_wyniku.delete(0, tk.END)
        pole_wyniku.insert(tk.END, str(wynik))
    except Exception as e:
        pole_wyniku.delete(0, tk.END)
        pole_wyniku.insert(tk.END, "Błąd")

# Funkcja, która dodaje cyfrę lub operator do wyświetlacza
def kliknij(przycisk):
    obecna_wartosc = pole_wyniku.get()
    pole_wyniku.delete(0, tk.END)
    pole_wyniku.insert(tk.END, obecna_wartosc + str(przycisk))

# Funkcja, która czyści wyświetlacz
def wyczysc():
    pole_wyniku.delete(0, tk.END)

# Tworzenie głównego okna
okno = tk.Tk()
okno.title("Kalkulator")

# Pole do wyświetlania wyników
pole_wyniku = tk.Entry(okno, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
pole_wyniku.grid(row=0, column=0, columnspan=4)

# Przycisk i jego przypisanie do odpowiednich funkcji
przyciski = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Tworzenie przycisków
for (przycisk, rzad, kolumna) in przyciski:
    if przycisk == '=':
        tk.Button(okno, text=przycisk, width=5, height=2, font=('Arial', 18),
                  command=oblicz).grid(row=rzad, column=kolumna)
    else:
        tk.Button(okno, text=przycisk, width=5, height=2, font=('Arial', 18),
                  command=lambda przycisk=przycisk: kliknij(przycisk)).grid(row=rzad, column=kolumna)

# Przycisk czyszczenia
tk.Button(okno, text='C', width=5, height=2, font=('Arial', 18),
          command=wyczysc).grid(row=4, column=2)

# Pole wyboru trybu ONP
tryb_onp = tk.BooleanVar()
checkbox_onp = tk.Checkbutton(okno, text="Tryb ONP", variable=tryb_onp)
checkbox_onp.grid(row=5, column=0, columnspan=4)

# Uruchomienie głównej pętli aplikacji
okno.mainloop()
