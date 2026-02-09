import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display.append("_")

lives = 6
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word.")
        if lives == 0:
            game_over = True
            print("You lose 😢")

    print(" ".join(display))
    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win 🎉")
