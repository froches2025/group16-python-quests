def personalized_greeting(name, quest):
    print("Greetings, " + name + "!")
    print("Your quest is: " + quest)
    print("Good luck on your journey!")
user_name = input("What is your name? ")
user_quest = input("What is your quest? ")
personalized_greeting(user_name, user_quest)
