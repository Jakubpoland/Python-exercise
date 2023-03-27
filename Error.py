try:
    print(x)
except NameError:
    print("Nie zdefiniowano zmiennej. Proszę ją podać: ")
    x = input()
finally:
    print(x)
