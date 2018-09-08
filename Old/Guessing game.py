import random
number = random.randint (1,20)
i=0
print ('I am thinking about a number between 1 and 20. Can you guess what it is?')
guess = int(input ())   #input is a string, need to convert it to int

while number != guess:
    if number > guess:
        i=i+1
        print ('Your guess is too low. You used '+ str(i) + ' attempts. Try again')
        guess = int(input ())
        continue #Need to tell computer to return back to while loop
    elif number < guess:
        i=i+1 #Up the counter before reporting back
        print ('Your guess is too high. You used '+ str(i) + ' attempts. Try again') #dont need to up the counter again
        guess = int(input ())
        continue
    else:
        break
i=i+1
print ('That is correct! You guessed it in ' + str (i) + ' guesses')