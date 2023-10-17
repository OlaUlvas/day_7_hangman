import random
from hangman_art import logo, stages
from hangman_words import word_list

display = []
wrong_letters = []
print("\nWelcome to the game")
print(logo)
random_word = random.choice(word_list)
print(f"\nPsst...the word is {random_word}")
for letter in random_word:
    display += "_"


lives = 6

game_on = True
while game_on:
    print(display)
    guess = input("\nEnter a letter: \n")
    if guess in display:
        print(f"You have already guessed {guess}, try another letter.")
    for position in range(len(random_word)):
        letter = random_word[position]
        if guess == letter:
            display[position] = letter
    if guess not in display:
        if guess in wrong_letters:
            print(f"You have already guessed {guess}, try another letter.")
        else:
            lives -= 1
            wrong_letters += guess
        if lives == 0:
            game_on = False
            print("You lose.")
            print(f"The right word was {random_word}.")
    if "_" not in display:
        print("You win.")
        game_on = False
        print(f"The right word was {random_word}.")

    print(stages[lives])



