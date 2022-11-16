import random

print("""
The program chooses persons for the stand-up in order
*****************************************************
1. Max
2. Priscllah
3. Patrick
4. Paul
5.
""")
number_present = 4
initial_number = 0
valid_choices = ["MAX", "PRISCILLAH", "PAUL","PATRICK"]

for initial_number in range(number_present):

    computer_choice = random.choice(valid_choices)
    msg = f'person choosen is {computer_choice}'
    print(msg)


