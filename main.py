from tkinter import *
from PIL import Image, ImageTk

random_word = 'game'
"""Predefine a random word and the number of attempts"""
guessed_letters = set()

import tkinter as tk

def play_multiplayer():
    # Clear all widgets inside the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Add a new label and entry field
    new_label = tk.Label(frame, text="Choose a word for your player:", font=("Arial", 12))
    new_label.pack(pady=5)

    new_typed_word = tk.Entry(frame, font=("Arial", 12))
    new_typed_word.pack(pady=5)
    submit_btn = tk.Button(frame, text="Submit", command= lambda: start_multiplayer(new_typed_word.get()))
    submit_btn.pack(pady=5)

def line_definition(word: str, guessed_letters: set):
    """Show guessed letters and hides others with '*'."""
    return ''.join(char if char.lower() in guessed_letters else '*' for char in word)

def open_final_screen():
    global image

    for widget in frame.winfo_children():
        widget.destroy()

    image = Image.open("img/congrats.jpg")
    image = image.resize((300, 150))  
    image = ImageTk.PhotoImage(image)

    label = tk.Label(frame, image=image)
    label.pack()


def start_multiplayer(typed_word):
    for widget in frame.winfo_children():
        widget.destroy()

    #Show the new world as '*
    new_label = tk.Label(frame, text=f'Your random word has {len(typed_word)} letters')
    masked_word = tk.Label(frame, text=line_definition(typed_word, guessed_letters))
    typed_letter = tk.Entry(frame, font=("Arial", 12))
    submit_btn = tk.Button(frame, text="Submit", command=lambda: check(typed_letter,masked_word, typed_word))


    submit_btn.pack(pady=5)
    typed_letter.pack(pady=5)
    new_label.pack(pady=5)
    masked_word.pack()
    

def start_solo():
    # Clear all widgets inside the frame
    for widget in frame.winfo_children():
        widget.destroy()

    #Show the new world as '*
    new_label = tk.Label(frame, text=f'Your random word has {len(random_word)} letters')
    masked_word = tk.Label(frame, text=line_definition(random_word, guessed_letters))
    typed_letter = tk.Entry(frame, font=("Arial", 12))
    submit_btn = tk.Button(frame, text="Submit", command=lambda: check(typed_letter, masked_word, random_word))


    submit_btn.pack(pady=5)
    typed_letter.pack(pady=5)
    new_label.pack(pady=5)
    masked_word.pack()
    

def check(letter, masked, word):
    # letter.delete(0, tk.END)
    global current_label

    if len(letter.get()) > 1 or letter.get().isalpha == False:
        invalid_letter_message = tk.Label(frame, text='Please type a valid letter', fg="red")
        invalid_letter_message.pack(pady=5)
        root.after(3000, invalid_letter_message.destroy)


    if letter.get() in word:
        masked.destroy()
        if current_label:
            current_label.destroy()
        
        guessed_letters.add(letter.get())
        masked_word = tk.Label(frame, text=line_definition(word, guessed_letters))
        masked_word.pack()
        current_label = masked_word

        """Verify if the user already have guessed all the letters in the random word"""  
        if '*' not in masked_word.cget("text"):
            print("Congratulations! You guessed the word!")
            open_final_screen()
        
    else:
        nice_try_message = tk.Label(frame, text="Nice try, but this letter is not in the word", fg="orange")
        nice_try_message.pack(pady=5)
        root.after(3000, nice_try_message.destroy)


    letter.delete(0, tk.END)


# Create main window
root = tk.Tk()
root.geometry("300x200")
current_label = None

# Create a frame
frame = tk.Frame(root, bg="lightblue")
frame.pack(fill="both", expand=True)

# Initial content
initial_label = tk.Label(frame, text="Choose your game mode", font=("Arial", 12))
initial_label.pack(pady=10)

btn_play_solo = tk.Button(frame, text="Play Solo", command=start_solo)
btn_play_solo.pack(pady=10)

btn_play_multiplayer = tk.Button(frame, text="Play Multiplayer", command=play_multiplayer)
btn_play_multiplayer.pack(pady=10)

root.mainloop()


"""Start with a welcome message and reveal the number of characters of the random word"""
# msg = Label(widget1, text="Welcome to the HangMan Game")


# game_choice = input('type 1 for solo or 2 for multiplayer option ')
# match game_choice:
#     case "1":
#         print(f'Your random word has', len(random_word) ,'characters')
#     case "2":
#         random_word = input('Type the random word you want - ')


"""start the attempts until it gets 15 trys using a loop strucutre with 'while' """
# while attempts > 0:

#     typed_letter = input('\nPlease put one letter - ').strip().lower()
#     os.system('cls')


#     """Check if the typed letter is a valid value"""
#     if len(typed_letter) != 1 or typed_letter.isalpha == False:
#         print('Please type a valid letter')
#         continue

#     if(typed_letter in guessed_letters):
#         print('You already try this letter, please type another one')
#         continue

#     """Check if there is the typed value in the random word"""
#     if typed_letter in random_word:
#         print('Gotcha!')
#         guessed_letters.add(typed_letter)
#         masked_word = line_definition(random_word, guessed_letters)
#         print(masked_word)
#     else:
#         print('Nice try, but this letter is not in the word')
#         masked_word = line_definition(random_word, guessed_letters)
#         print(masked_word)

#     """Verify if the user already have guessed all the letters in the random word"""  
#     if '*' not in masked_word:
#         print("Congratulations! You guessed the word!")
#         break

#     attempts -= 1
#     if attempts > 0 :
#         print(f'you still have {attempts} attempts')
#     else:
#         print('sorry but your trys ends')