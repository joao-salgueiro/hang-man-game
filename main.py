import os

def line_definition(word: str, guessed_letters: set):
    """Reveals guessed letters and hides others with '*'."""
    return ''.join(char if char.lower() in guessed_letters else '*' for char in word)



"""Predefine a random word and the number of attempts"""
random_word = 'game'
attempts = 15
guessed_letters = set()


"""Start with a welcome message and reveal the number of characters of the random word"""
print('Welcome to the HangMan Game \n')
print('Do you want to play solo ? Or maybe you want to type a word for someone to try ? type 1 or 2 - ')
game_choice = input('type 1 for solo or 2 for multiplayer option ')

match game_choice:
    case "1":
        print(f'Your random word has', len(random_word) ,'characters')
    case "2":
        random_word = input('Type the random word you want - ')


"""start the attempts until it gets 15 trys"""
while attempts > 0:

    typed_letter = input('\nPlease put one letter - ').strip().lower()
    os.system('cls')


    """Check if the typed letter is a valid value"""
    if len(typed_letter) != 1 or typed_letter.isalpha == False:
        print('Please type a valid letter')
        continue

    if(typed_letter in guessed_letters):
        print('You already try this letter, please type another one')
        continue

    """Check if there is the typed value in the random word"""
    if typed_letter in random_word:
        print('Gotcha!')
        guessed_letters.add(typed_letter)
        masked_word = line_definition(random_word, guessed_letters)
        print(masked_word)
    else:
        print('Nice try, but this letter is not in the word')
        print(masked_word)

    """Verify if the user already have guessed all the letters in the random word"""  
    if '*' not in masked_word:
        print("Congratulations! You guessed the word!")
        break

    attempts -= 1
    if attempts > 0 :
        print(f'you still have {attempts} attempts')
    else:
        print('sorry but your trys ends')