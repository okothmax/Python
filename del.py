class Robot():
    number = 0
    def __init__(self, name):
        self.name = name
        type(self).number += 1

    def __del__(self):
        type(self).number -= 1
        print (self.name + " says bye-bye!")

if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    print(Robot.number)
    z = x
    print(Robot.number)
    print("Deleting x")
    del x
    print(Robot.number)
    print("Deleting z")
    del z
    print(Robot.number)
    del y
    print(Robot.number)
