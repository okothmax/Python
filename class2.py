class C(object):
    def __init__(self,c = 10,d = 42):
        self.c = c
 
        # d is private instance variable
        self.__d = d
 
 
class D(C):
    def __init__(self, e = 84):
        self.e = e
        super().__init__(c,d)
 
 
object1 = D()
 
# produces an error as d is private instance variable
print(object1.d)