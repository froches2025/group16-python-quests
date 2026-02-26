print("=" * 50)
print("WELCOME TO THE LOOP OF RIDDLES")
print("=" * 50)
print("I'm thinking of a secret number...")
print("It's between 1 and 10.")
print("Think you can guess it? Let's find out!")
print("=" * 50)
secret_number = 9

print("Guess the secret number (1-10):")
guess = int(input("Your guess: "))

while guess != secret_number:
    if guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
    guess = int(input("Guess again: "))

print(f"Yes! The secret number was {secret_number}!")
