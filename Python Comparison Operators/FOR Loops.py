# for loops
# iteration = 

mylist=[1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)

mylist=[1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    #we will check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd Numbah: {num}")

mylist=[1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print(list_sum)

mylist=[1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
    print(list_sum)


#strings:

mystring = "hello world"
for letter in mystring:
    print(letter)

#Tuple unpacking

mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))
for (a,b) in mylist:
    print(a)
    print(b)

mylist = [(1,2),(3,4),(5,6),(7,8)]
for a,b in mylist:
    print(a)
    

# dictionary

d={'k1':1,'k2':2,'k3':3}
for item in d.items(): #items - for items values for values :) 
    print(item)


