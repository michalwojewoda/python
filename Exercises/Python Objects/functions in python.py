def name_function():
    '''
    DOC STRING: info     
    '''
    print("hello")

name_function()

help(name_function)

def say_hello(name='NAME'):
    return("hello "+name)
result = say_hello("jose")

#find out if the word dog is in a string

def dog_check(mystring):
    if "dog" in mystring.lower(): #this is a booleon - so
        return True
    else:
        return False
dog_check("dog ran away")


def do_check(s):
    return "dog" in s.lower()
do_check("dog ran away")


### PIG LATIN

def pit_latin(word):

    first_letter 