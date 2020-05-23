# Write a Python program to display the current date and time.
from datetime import date
today = date.today()
print("Curent date and time:", today)


#atempt 2

from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
print("Curent date and time is:\n", dt_string)

#different angle

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
