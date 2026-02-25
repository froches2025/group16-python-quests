# Quest 29: The Code Breaker
# Concept: Allow a user 3 attempts to guess the secret code.

secret_code = 42
attempts = 3

while attempts > 0:
    guess = int(input(f"Guess the secret code. You have {attempts} attempt(s) left: "))
    
    if guess == secret_code:
        print("Correct! You guessed the code!")
        break
    elif guess < secret_code:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    
    attempts -= 1

if attempts == 0:
    print(f"Game over! The secret code was {secret_code}.")
