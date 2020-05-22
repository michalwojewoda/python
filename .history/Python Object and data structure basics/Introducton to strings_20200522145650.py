
print("Hello World")
print("Hello \n World")
print("Hello \t World")
len("hello")
len("To be, or not to be, that is the question: \nWhether 'tis nobler in the mind to suffer \nThe slings and arrows of outrageous fortune, \nOr to take Arms against a Sea of troubles, \nAnd by opposing end them: to die, to sleep;")
print("To be, or not to be, that is the question: \n \t Whether 'tis nobler in the mind to suffer \n \t\t The slings and arrows of outrageous fortune, \n \t\t\tOr to take Arms against a Sea of troubles, \nAnd by opposing end them: to die, to sleep;")


#Indexing and slicing strings

mystring="abcdefghijk"
print(mystring)
print(mystring[::-1])
print(mystring[2:7:2])


# Formatting with the .format() method

print('This is a string {}'.format('INSERTED'))
print('The {2} {1} {0}'.format('fox','brown',"quick"))
print('The {q} {q} {f}'.format(f='fox',b="brown",q="quick"))

# Float formatting Follows "{value:width.precision f}"

result = 100/777
print(result)
print("The result is {}".format(result))