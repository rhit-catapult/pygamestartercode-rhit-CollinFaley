import random

print("guess my number")


secret_number = random.randint(1,100)


counter = 0


while True:
  counter += 1
  guess = int(input("guess a number (1-100): "))
  if guess > secret_number:
    print(guess, "is too high, guess lower")
  if guess < secret_number:
    print(guess,"is too low, guess higher")
  if guess == secret_number:
    print(guess, f"congrats you did it in {counter} tries")
    break

print("goodbye")

if guess == 1:
  print("lucky guess")

