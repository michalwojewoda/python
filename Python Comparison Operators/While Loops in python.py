#while loops will continue to execute a block of code while some conditions remains True.
#for examle, while my pool is not full, keep fillling my pool with water,
# While my dogs are still hungry, keep feeding my dogs 

x = 0 
while x < 5:
    print(f'the current value of x is {x}')
    x += 1
else:
    print("X is not less than 5")

#Break, continue, pass

x = [1,2,3]
for item in x:
    pass
print('end of my script')

mystring = "sammy"
for letter in mystring:
    if letter == "a":
        continue
    print("letter")

mystring = "sammy"
for letter in mystring:
    if letter == "a":
        break
    print("letter")