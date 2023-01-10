import random

number = random.randint(1, 10)

guess = int(input("Guess a number from 1 to 10: "))

while guess != number:
    print("Your guess was incorrect. Please try again.")
    guess = int(input("Guess a number from 1 to 10: "))

print("Your guess was correct. Congratulations!")