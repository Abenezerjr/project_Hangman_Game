import random
from hangman_art import logo,stages
from hangman_words import word_list

print(logo)

# word_list =
no_more = True
lives = 6
chosen_word = random.choice(word_list)

print(chosen_word)


display = []
for _ in range(len(chosen_word)):
    display += "_"

while no_more:

    guess = input("guess a letter: ").lower()
    if guess in display:
        print(f" you've already guessed {guess}")


    # Todo-3
    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if guess == letter:
            display[position] = letter
    if guess not in chosen_word:

        lives -= 1
        print(f" your guess {guess} is not in the letter now you have: {lives} lives")
        if lives == 0:
            no_more = False
            print("You lose")

    print(f"{''.join(display)}")
    if "_" not in display:
        no_more = False
        print("you win")
    print(stages[lives])


