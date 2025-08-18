# Hang Man game

words = ["banana", "apple", "orange", "grape", "kiwi",
          "lion", "tiger", "panther", "zebra", "rino",
            "whale", "dolphin", "starfish", "shark", "octopus",
              "eagle", "falcon", "vulture", "ostrich", "pigeon"]

list1 = ["banana", "apple", "orange", "grape", "kiwi"]
list2 = ["lion", "tiger", "panther", "zebra", "rino"]
list3 = ["whale", "dolphin", "starfish", "shark", "octopus"]
list4 = ["eagle", "falcon", "vulture", "ostrich", "pigeon"]

import random

hangman_art = {
    0: ('''
     +---+
     |   |
         |
         |
         |
         |
    ========='''),

    1: ('''
     +---+
     |   |
     O   |
         |
         |
         |
    ========='''),

    2: ('''
     +---+
     |   |
     O   |
     |   |
         |
         |
    ========='''),

    3: ('''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    ========='''),

    4: ('''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    ========='''),

    5: ('''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    ========='''),

    6: ('''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========''')
}


def display_man(wrong_guesses):
    print('******************')
    print(hangman_art[wrong_guesses])
    print('******************')

def display_hint(hint):
    print(' '.join(hint))
        

def display_answer(answer):
    print(' '.join(answer))

def main():
    answer = random.choice(words)
    if answer in list1:
        print('It is a  Fruit')
    
    if answer in list2:
        print('It is an Animal')
    
    if answer in list3:
        print('It is an Aquatic Animal')

    if answer in list4:
        print('It is a Bird')
    
    hint = ['_'] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()

    while True:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input('Enter a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invaild choice")
            continue

        if guess in guessed_letters:
            print(f'{guess} is already guessed')
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        
        if wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            print('-------YOU LOSE😞-------')
            break

        if '_' not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print('-------YOU WIN!🥳-------')
            break


if __name__ == "__main__":
    main()

# End of Hangmna game