# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if not letter in letters_guessed:
            return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = []
    for letter in secret_word:
        if letter not in letters_guessed:
            guessed_word.append("_ ")
        else:
            guessed_word.append(letter)

    return ''.join(guessed_word)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters_list = []
    for letter in string.ascii_lowercase:
        if not letter in letters_guessed:
            available_letters_list.append(letter)

    return ''.join(available_letters_list)


def get_guessed_letter(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, the letter that the user guesses. Or none if she runs out of warnings
    '''
    warnings = 3

    while True:
        guess = input('Please guess a letter: ')
        if guess == "*":
            return guess

        elif not guess.isalpha():
            warnings -= 1
            print(f"Oops! That is not a valid letter. You now have {warnings} warnings")

            if warnings == 0:
                return None
            else:
                continue

        guess = guess.lower()

        if guess in letters_guessed:
            warnings -= 1
            print(f"Oops! You've already guessed that letter. You now have {warnings} warnings")
            if warnings == 0:
                return None
            else:
                continue

        return guess


def get_score(secret_word, guesses_left):
    '''
    secret_word: string, the word the user is guessing
    guesses_left: integer, the amount of guesses remaining after the game is over
    returns: integer, the product of the number of unique letters in the secret word and the guesses remaining
    '''
    unique_letters = []
    for letter in secret_word:
        if not letter in unique_letters:
            unique_letters.append(letter)

    word_score = len(unique_letters)
    total_score = word_score * guesses_left

    return total_score




def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    pass

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    word = my_word.replace(' ','')
    if len(word) != len(other_word):
        return False

    for i, letter in enumerate(word):
        if letter == '_' and other_word[i] not in letters_guessed:
            continue
        else:
            if word[i] != other_word[i]:
                return False
    
    return True


def show_possible_matches(my_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matching_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word, letters_guessed):
            matching_words.append(word)
            
    return matching_words


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 6
    letters_guessed = []
    vowels = 'aeiou'
    print(f"""
Welcome to the game Hangman!
I am thinking of a word that is {len(secret_word)} letters long.
          """)

    while not is_word_guessed(secret_word, letters_guessed) and guesses_left > 0:
        print(f"""
----------------------
You have {guesses_left} guesses left.
Available letters: {get_available_letters(letters_guessed)}            
              """)

        guess = get_guessed_letter(letters_guessed)
        if guess == None:
            print("You have no warnings left, so you lose a guess")
            guesses_left -= 1
            continue

        letters_guessed.append(guess)
        my_word = get_guessed_word(secret_word, letters_guessed)
        if guess == "*":
            print(f"""
Possible word matches are:
{show_possible_matches(my_word, letters_guessed)}
                  """)

        elif guess in secret_word:
            print(f"Good guess!: {my_word}")

        else:
            if guess in vowels:
                guesses_left -= 2
            else:
                guesses_left -= 1
            print(f"Oops! That letter is not in my word: {my_word}")
            continue

    if is_word_guessed(secret_word, letters_guessed):
        print(f"""
----------------------
Congratulations, you won!
Your total score for this game is: {get_score(secret_word, guesses_left)}""")
    else:
        print(f"""
----------------------
Sorry, you ran out of guesses. The word was {secret_word}
""")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
