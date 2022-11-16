import random
print("""
ALX BUDDIES
************

MEMBERS
1. Maxwell
2. Priscillah
3. Robert
4. paul
5. caroline
6. Patrick
7. Double O
""")
People = ["Maxwell", "Priscillah", "Robert", "Paul", "Caroline", "Patrick", "Double O"]
choice = random.choice(People).upper()
print("LETS PICK A PERSON TO CREATE THE LINK")
print("########################################")
print(f"The person choosen is ***{choice}***")

