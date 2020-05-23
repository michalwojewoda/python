# Write a Python program to accept a filename from the user and print the extension of that.
filename = input("Please input here the Filename: \n")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))