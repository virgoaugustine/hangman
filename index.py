# Hangman Game
import random 
import os

clear = lambda : os.system('clear')



def play_hangman():
    with open ('words.txt','r') as file:
        words = file.read().split('\n')

    random_word = random.choice(words).lower()
    word_holder = "*".lower() * len(random_word)
    attempts = 5
    print(word_holder)

    while attempts > 0:

        user_input = input('Enter a letter: ').lower()

        if user_input in random_word:
            for i in range(len(random_word)):
                if random_word[i] == user_input:
                    word_holder = word_holder[:i] + user_input + word_holder[i+1:]
            print(word_holder)
        else:
            attempts -= 1
            print('Letter not in word. {} attempts left.'.format(attempts))
            if attempts == 0:
                clear()
                print("You have no attempts left. Please start again")
                play_hangman()

        if random_word == word_holder:
            break
    print("You guessed the correct word. Congrats")

if __name__ == "__main__":
  
    play_hangman()
