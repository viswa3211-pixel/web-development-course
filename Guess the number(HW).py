import random

print("Enter your name:- ")
name = input()

number = random.randint(1, 100)
attempts = 5

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")
print("You only have 5 attempts.")

for i in range(attempts):
    guess = int(input("Enter your guess: "))

    # Check if correct
    if guess == number:
        print("🎉 Congratulations!" + name + ", you guessed the number.")
        print("You guessed it in", i + 1, "attempts.")
        break

    # Check how close the guess is
    difference = abs(number - guess)

    if difference <= 5:
        print("🔥 Very close!")
    elif difference <= 10:
        print("👍 Close!")

    # High / Low hint
    if guess < number:
        print("Too low!")
    else:
        print("Too high!")

    print("Attempts left:", attempts - (i + 1))

# If user fails all attempts
if guess != number:
    print("❌ Game Over! " + name + ", the correct number was:", number)