print("""
THIS IS A SIMPLE CAR GAME
*************************
Use the following commands to play the game
1. START -> to start the car
2. STOP -> to stop the car
3. QUIT -> to quit the game 
4. HELP -> to view the commands
""")
command_input = input("Enter the command: ").upper()
STARTED = False
while True:
    if command_input == "START":
        if STARTED:
            print("the car is already started")
        else:
            STARTED = False
            print("the car started")
            break
    elif command_input == "STOP":
        if not STARTED:
            print("the car is alredy stopped")
            break
        else:
            STARTED = False
            print("the car is stopped")
    elif command_input == "HELP":
        print("""
        START - to stop the car
        STOP - to stop the car
        QUIT - to quit the game 
        """)
        break
    elif command_input == "QUIT":
        break
    else:
        print("invalid command")
        break
