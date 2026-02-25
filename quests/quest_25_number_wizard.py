# Quest 25: The Number Wizard

secret_number = 7
guess = int(input("Guess the magic number: "))

while guess != secret_number:

    if guess > secret_number:
        print("Too high!")
    else:
        print("Too low!")

    guess = int(input("Try again: "))

print("🎉 Correct! You are a true Number Wizard!")