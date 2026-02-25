# Quest 24: The Master Spell
# Concept: Calling a function from within another function.

def ask_for_age():
    age = int(input("What is your age? "))
    return age

def can_they_vote(age):
    if age >= 18:
        print("You are old enough to vote!")
    else:
        print("You are not old enough to vote yet.")

# Call ask_for_age and pass its result to can_they_vote
voter_age = ask_for_age()
can_they_vote(voter_age)
