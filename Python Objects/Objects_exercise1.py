# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd¶

def myfunc(a,b):
    if a%2 == 0 and b%2 == 0:
        if a > b:
            return b
        else:
            return a
    else:
        if a < b:
            return b
        else:
            return a
    return(myfunc)

print(myfunc(2,5))


def returners(a,b):
    if a%2 == 0 and b%2 == 0:
        result = min(a,b)
    else:
        result = max(a,b)
    return(result)

print(returners(2,3))