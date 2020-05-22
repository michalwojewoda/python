# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input("Please, state your name: ")
age = input("Please, state your age:  ")
age = int(age)
year = str((2020 - age)+100)
print(name + " you will turn 100 years in: " + year)

# clear code and make it "time proof"

name = input("Please, state your name: ")
age = int(input("Please, state your age: "))
import time
year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())
year = str(year + (100 - age))
print(name + " , you will turn 100 in year" + year)

# fuck around with the code

name = input("\n Sir, Sir, \n \t Please, tell me who you are: \n")
age = int(input("\n Och, nice to meet you \n \tTel me your Age, and i will tell you a secret! \n "))
import time
year, min = map(int, time.strftime("%Y"))
year = str(year + (100 - age))
print(name + " the big secret of your life is that you will end 100 in year " + year )
