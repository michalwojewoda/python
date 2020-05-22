my_list = ["one","two","three"]
print(len(my_list))
print(my_list[0]) #indexing
print(my_list[1:]) #conc
another_list = ['four',"five"]
new_list = my_list + another_list
print(new_list)
new_list[0] = 'ONE ALL CAPS'
print(new_list)
new_list.append("six")
print(new_list)
# removing things from the list
new_list.pop()
print(new_list)
popped_item = new_list.pop()
print(popped_item)

#source and reverse 

newlist = ["a","e","x","d","h","i"]
num_list = [4,1,8,3]
print(newlist.sort())
print(newlist)

print(num_list.reverse)
print(num_list)