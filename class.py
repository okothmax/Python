class Animal:

    all = []
    count = 0
    def __init__(self, name, age):
        assert type(name) == str
        assert type(age) == int
        self.__name = name
        self.age = age
        type(self).all.append(self)
        type(self).count += 1

    @property
    def name(self):
        return(self.__name)
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return(self.__age)
    
    @age.setter
    def age(self, value):
        self.__age = value

    def __repr__(self):
        return (f'Animal("{self.name}", {self.age})')

class Wild(Animal):
    count1 = 0
    def __init__(self, name, age, domestic):
        super().__init__(
            name, age
        )
        self.domestic = domestic
        type(self).count1 +=1

dog = Animal("rose", 12)
cat = Animal("cute", 45)
cat.name = "joe"
print(cat.name)
cat.domestic = 'yes'
parrot = Wild("ok", 20, 'no')
dog.name = 'mike'
print(dog.name)
print(dog.age)
print(parrot.domestic)
print(Wild.count1) 