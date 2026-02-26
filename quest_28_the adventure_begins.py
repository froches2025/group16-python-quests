def start():
    print("\nYou're in a dark forest. You see a cave and a river.")
    choice = input("Do you go to the CAVE or follow the RIVER? ").lower()
    
    if choice == "cave":
        cave()
    elif choice == "river":
        river()
    else:
        print("Invalid choice!")
        start()

def cave():
    print("\nYou enter the cave and find treasure!")
    print("But a dragon wakes up and chases you out!")
    print("ENDING 1: You escape with one gold coin - barely!")
    play_again()

def river():
    print("\nYou follow the river and find a hidden village.")
    print("The villagers welcome you and you start a new life.")
    print("ENDING 2: You found a new home!")
    play_again()

def play_again():
    if input("Play again? (yes/no): ").lower() == "yes":
        start()
    else:
        print("Thanks for playing!")

start()
