"""
In this a user who pick the magic number wins the game 
Each user is given thre chances to pick the right maguc number
All the best
****************************************************************
"""
magic_number = 5
choices_count = 0
choice_max = 3
print("""
The vaild choices are:
1, 2, 3, 4, 5, 6, 7, 8, 9
""")
while (choices_count < choice_max):
    user_choice = int(input("Pick a number: "))
    if (user_choice == magic_number):
        print("YOU WIN!!!!")
        break
    else:
        print("NOT YET")
    choices_count+=1
