#key words:
# If / elif / else 
# If some_condition 
#      #execute some code
    #elif 
        #do smth else
    # else"
        #do something else


if 3>2: 
    print("It is true")

hungry = False
if hungry:
    print("Feed the dog")
else:
    print("Dog Lies")

loc = "bank"
if loc == "Auto shop":
    print("Cars rules the world")
elif loc == "bank":
    print("Wallstreet rules the world")
else:
    print("Why do you ask?")


name = 'Joslin'
if name == 'sammy':
    print("It is nice to meet you sammy")
elif name == "John":
    print("Hello John")
else:
    print("What is your name?")




'''In this program, we input a number
check if the number is positive or
negative or zero and display
an appropriate message
This time we use nested if statement'''

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")