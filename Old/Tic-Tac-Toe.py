Board = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ', 
         'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
         'bot-l': ' ', 'bot-m': ' ', 'bot-r': ' '}

def printBoard (Board):
    print (Board ['top-l'] + '|'+ Board ['top-m'] +'|'+ Board ['top-r'])
    print ("-+-+-")
    print (Board ['mid-l'] + '|'+ Board ['mid-m'] +'|'+ Board ['mid-r'])
    print ("-+-+-")
    print (Board ['bot-l'] + '|'+ Board ['bot-m'] +'|'+ Board ['bot-r'])
    
turn = 'X'
for i in range (9):
    print ('It is turn of ' + turn + ' What is your turn?')
    pos = input ()
    Board [pos] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    printBoard(Board)
    
print ('Game over.')