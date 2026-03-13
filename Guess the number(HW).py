import random

my_name = input("Please enter your name: ")

# Computer selects a random number
number = random.randint(1, 100)

attempts = 5

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")
print("You only have 5 attempts.")

for i in range(attempts):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Congratulations!" + my_name + "! You guessed the number.")
        print("You guessed it in", i+1, "attempts.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

    print("Attempts left:", attempts - (i+1))

if guess != number:
    print("Better luck next time! "+ my_name + " ❌ Game Over! The correct number was:", number)