import random

print("guess my word")


def update_display_word(newest_guess, secret_word, display_word):
    result = ""
    for k in range(len(display_word)):
        if newest_guess == secret_word[k]:
            result += newest_guess
        else:
            result += display_word[k]
    return result


words = ["catapult", "funishment", "rose", "hulman", "fisher"]

# pick a random word
# initialized the display word in the correct lenghth *
# start loop
#   ask user to guess a letter
#   check the letter (have they guessed it already)
#   check the letter (see if it is in secret_word)
#   update display word to show the letters
#   check for gameover if display word = secret word), break


secret_word = random.choice(words)
display_word = "*" * len(secret_word)
guessed_letter = []

print(display_word)

while True:
    print()
    guess = input("guess a letter ")
    print(guessed_letter)
    if guess in guessed_letter:
        print("you did that already")
        continue

    guessed_letter.append(guess)
    display_word = update_display_word(guess, secret_word, display_word)
    print(guessed_letter)
    print(display_word)
    if display_word == secret_word:
        break

print(f"you got it in {len(guessed_letter)}")
