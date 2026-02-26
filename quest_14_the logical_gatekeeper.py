age = int(input("How old are you? "))
gold = int(input("How many gold coins do you have? "))
if age >= 18 and gold >= 20:
    print("Welcome to the club! Enjoy your night.")
    
else:    print("Sorry, you do not meet the requirements to enter the club.")
if age < 18:
    print("You must be at least 18 years old to enter the club.")
if gold < 20:
    print("You must have at least 20 gold coins to enter the club.")
    