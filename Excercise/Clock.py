import datetime
import time
while True:
    x = datetime.datetime.now()
    print(x.strftime("%c"))
    time.sleep(1)
