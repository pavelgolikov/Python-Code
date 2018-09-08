# This code gives 5 attempts at a password after a user enters the right user name, then it breaks

print ('What is your name?')
name = input ()
if name == 'Joe':
    print ('Welcome Joe! You have 3 attempts to log in, after that you will be locked out.')
    for i in range (3):
        print ('Attemtp # ' + str (i+1) + '. What is the password?')
        password = input ()
        if password == 'Ray':
            print ('Welcome back Joe! Nice to see you.')
            break
        else:
            print ('Wrong password entered, you have ' + str (3-(i+1)) + ' attempts left.')
            if i == 2:
                print ('You have entered a wrong password 3 times, you are now locked out.')
else:
    print ('Wrong name.')                