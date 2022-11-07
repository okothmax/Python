import random
print("""
Choose one option from the three choices
****************************************
1. PAPER
2. ROCK
3. SCISSORS
""")
choice_count = 0
choice_count_limit = 3
valid_choices = ["ROCK", "PAPER", "SCISSORS"]
while (choice_count < choice_count_limit):
    user_choice = input("What is your choice: ")
    computer_choice = random.choice(valid_choices)
    person = user_choice.upper()
    comp = computer_choice.upper()
    
    if person in valid_choices:
        print(f"You have chosen {person}")
        print(f"Random choice is {comp}")
        if ((person == "ROCK" and comp == "ROCK") or (person == "PAPER" and comp == "PAPER") or (person == "SCISSORS" and comp == "SCISSORS" )):
            print("Its a tie")

        elif ((person == "ROCK" and comp == "SCISSORS") or (person == "SCISSORS" and comp == "PAPER") or (person == "PAPER" and comp == "ROCK")):
            print("YOU WIN!!!")

        else:
            print("YOU LOOSE")
        choice_count = choice_count + 1
    else:
        print("Invalid option. Try again")