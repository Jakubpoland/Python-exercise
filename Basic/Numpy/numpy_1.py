import numpy as np

"""
# Tworzenie tablicy jednowymiarowej
a = np.array([1, 2, 3])

# Tworzenie tablicy dwuwymiarowej
b = np.array([[1, 2, 3], [4, 5, 6]])

print(b[1,1])
"""

"""
# Dodawanie dwóch tablic
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b

print(c)
# Mnożenie tablic przez skalar
a = np.array([1, 2, 3])
b = 2 * a
print(b)
# Mnożenie dwóch tablic element po elemencie
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a * b
print(c)
# Obliczanie średniej tablicy
a = np.array([1, 2, 3, 4, 5])
mean_a = np.mean(a)
print(mean_a)
"""

# Indeksowanie tablicy
a = np.array([1, 2, 3])
print(a[0])  # wyświetli 1

# Wycinanie fragmentu tablicy
a = np.array([1, 2, 3, 4, 5])
b = a[1:4]  # b to [2, 3, 4] Od 2 do 3 Nie bierzemy 1 i 4
print(b)