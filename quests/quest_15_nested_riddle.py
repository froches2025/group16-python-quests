# Quest 15: The Nested Riddle
# Concept: Nested if Statements - An if statement inside another.

choice = input("Do you go left or right? ")

if choice == "left":
    action = input("Do you swim or wait? ")
    if action == "swim":
        print("You find a treasure chest! You win!")
    else:
        print("You wait and a crocodile appears. Game over!")
elif choice == "right":
    print("You fall into a pit. Game over!")
else:
    print("Invalid choice. Game over!")
