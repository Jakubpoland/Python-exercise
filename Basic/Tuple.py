# Tworzenie tupli
tup1 = (1, 2, 3, 4)
tup2 = ('a', 'b', 'c', 'd')

# Wypisanie tupli
print(tup1)  # (1, 2, 3)

# Dostęp do elementów tupli
print(tup1[0])  # 1

# Wypisanie od drugiego do trzeciego
print(tup1[1:3])

# Łączenie tupli
tup3 = tup1 + tup2
print(tup3)  # (1, 2, 3, 'a', 'b', 'c')

# Rozpakowywanie tupli
x, y, z, w= tup1
print(x)  # 1
print(y)  # 2
print(z)  # 3
print(w)  # 4

# Tuple jako klucze w słowniku
d = {(1, 2): 'a', (3, 4): 'b'}
print(d[(1, 2)])  # 'a'
