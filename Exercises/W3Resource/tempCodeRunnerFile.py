def fibonacci():
	n = int(input("How many Fibonacci's numbers would you like to generate? "))
	fib = [0, 1]
	for i in range(2, n):
		fib.append(fib[-1] + fib[-2])
	print (len(fib))
	return fib
print (fibonacci())