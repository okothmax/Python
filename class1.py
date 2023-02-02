class Animal:

    #creating class variables
    no_of_instances = 0
    animals = []

    def __init__(self, age: int, color: str):
        self.__age = age 
        self.__color = color
        type(self).no_of_instances +=1       #Animal
        type(self).animals.append(self)

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self__age = value

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value):
        self.__color = value

    @classmethod
    def printNumber(cls):
        return (cls.no_of_instances)
    
    @staticmethod
    def greaterAge(value1, value2):
        return value1 > value2
    
    @classmethod
    def allAnimals(cls):
        return cls.animals
    
    # creating a string  representation
    def __repr__(self):
        return f'Animal({self.age}, "{self.color}")'
    
  

class Domestic(Animal):
    def __init__(self, age: int, color: str, domestic: bool):
        super(). __init__(
            age, color
        )
        self.__domestic = domestic

    #polymorphism -> there is another function in the parent class Animal    
    def __repr__(self):
        return f'Domestic({self.age}, "{self.color}", {self.__domestic})'
    
    def sendEmail(self):
        connectToServer()

        return "send email"

    # abstraction
    def __connectToServer(self):
        pass

#creating a sub-class (child class)
class meatEater(Domestic):
    def __init__(self, age: int, color: str, domestic: bool, Eating: bool):
        #using the super() to add attributes of the parent class
        super().__init__(
            age, color, domestic
        )
        #creating a private attribute 
        self.__Eating = Eating

#creating an instance of meatEater
cockroarch = meatEater(4, "red", True, False)

#accessing the class variable under the class variable 
print(meatEater.no_of_instances)