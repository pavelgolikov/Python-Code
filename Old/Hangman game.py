"""Game of Hangman."""


#Helper functions:
import string
secret_word = 'apple'
letters_guessed = []

def is_word_guessed (secret_word, letters_guessed):
    for char in secret_word:
        if char in letters_guessed:
            continue
        else:
            return False
            break
    return True

#function gets secret word and letters guessed, returns updated word with guessed letters
def get_guessed (secret_word, letters_guessed):
    string = ''
    for char in secret_word:
        if char in letters_guessed:
            string = string + char
        else:
            string = string + '_ '
    return string

def get_available_letters (letters_guessed):
    letters_available = ''
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            letters_available = letters_available + char
        else:
            continue
    return letters_available

def is_vowel(guess):
    vowels = ['a', '​e', 'i', 'o', 'u']
    if guess in vowels:
        return True



def Hangman (secret_word):
    letters_guessed = []
    guesses = 6
    warnings = 3
    print ('Welcome to the game Hangman')
    print ('I am thinking about a word that is ' + str(len(secret_word)) + ' letters long.')
    
    while guesses != 0:
        print ('---------------')
        print ('You have ' + str(guesses) + ' guesses left. \nAvailable letters are: ' + str(get_available_letters (letters_guessed)))
        print ('Please enter a guess?')
        guess = input()
        
        if guess.isalpha():
            if guess not in letters_guessed:
                letters_guessed = letters_guessed + [str.lower(guess)]
                if guess in secret_word:
                    print ("Good guess: " + get_guessed (secret_word, letters_guessed))
                    if is_word_guessed (secret_word, letters_guessed):
                        print ('Congratulations! You won. \nYour score is ' + str((len(secret_word))*(guesses)) + '.')
                        break
                else:
                    print ('Oooops, there is no such letter in a word I am thinking about.\n' + get_guessed (secret_word, letters_guessed))
                    if is_vowel(guess):
                        guesses -=2
                    else:
                        guesses -= 1
                    #Insert code or consonant vs vowel guess losses here
            else:
                if guess in secret_word:
                    print ('You have already correctly guessed this letter.')
                else:
                    if warnings != 0:
                        warnings -=1
                    else:
                        guesses -= 1
                    print ('You have already tried to guess this letter. You have ' + str(warnings) + ' warnings left.\n' + get_guessed (secret_word, letters_guessed))
                    continue
        else:
            if warnings != 0:
                warnings -=1
            else:
                guesses -= 1
            print (('You have entered an invalid entry, please enter a letter. You have ' + str(warnings) + ' warnings left.\n' + get_guessed (secret_word, letters_guessed)))
            continue
    if guesses == 0:
        print ('Sorry, you ran out of guesses, my word was "' + secret_word + '."')

Hangman(secret_word)