#Dodawanie liczb
"""
def dodajLiczby(l1, l2):
    #print(l1+l2)
    return l1 + l2

#dodajLiczby(2,3)
#dodajLiczby(6,5)
print(dodajLiczby(2,3))
print(dodajLiczby(5,2))
"""

#Pierwsza i ostatnia litera
"""
def ostatniaLitera(lancuch):
    return lancuch [len(lancuch)-1]
def pierwszaLitera(lancuch):
    return lancuch[0]

print("Pierwsza litera ", pierwszaLitera("Analityk"), "Ostatnia litera ", ostatniaLitera("Analityk"))
"""

#Zamiana Na wielkie
"""
def ZamianaNaWielkie(lancuch):
    return lancuch.upper()

lancuch=input()
print(ZamianaNaWielkie(lancuch))
"""

"""
def usunParzyste(lista):
    nowaLista=[]
    for i in lista:
        if i%2 != 0:
            nowaLista.append(i)
    return nowaLista

ll = [11,22,412,531,532,66,85]
print(usunParzyste(ll))
"""