#  Question 1: Accept two integer numbers from a user and
#  return their product and  if the product is greater than 1000,
#  then return their sum

def mult_or_sum(num1, num2):
    product = num1 * num2

    if (product <= 1000):
        return product
    else:
        return num1 + num2
    

number1 = int(input("Give number 1: "))
number2 = int(input("Give number 2: "))

result = mult_or_sum(number1, number2)
print("The result is: ", result)

