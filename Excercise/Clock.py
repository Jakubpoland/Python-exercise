import datetime
import time
while True:
    x = datetime.datetime.now() #Pobieranie daty i czasu
    print(x.strftime("%c")) #Wyświetlanie czasu
    time.sleep(1) #Czekanie 1 sekundy
