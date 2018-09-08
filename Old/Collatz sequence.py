"""Program to print Collatz sequence for an entered number."""


def Collatz (number):
    if number % 2 == 0:
        print (number // 2)
        return (number // 2)
    else:
        print (number*3 +1)
        return (number*3 +1)
    
def Collatzseq (number):
    while number != 1:
        number = Collatz (number)
        
print ('Please enter an integer.')
try:
    number = int (input ())
    Collatzseq (number)
except ValueError:
    print ('You have entered something other than integer. Please try again')
    number = int (input ())
    Collatzseq (number)