guess_times = 0
guessed_numbers = []
print('this is a game, guess 3 numbers between 1-49')
while guess_times < 3:              #while loop
    num = input('enter a number :')
    guessed_numbers.append(num)
    guess_times += 1

print(guessed_numbers)