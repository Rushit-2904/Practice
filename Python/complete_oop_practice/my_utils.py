class MyClass:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def func(self):

        return(f"numbers are {self.a},{self.b}")
    
    @staticmethod
    def func1(a,b):

        return(f"static method's numbers are {a},{b}")



class User:

    def login(self):
        print("login")

    def register(self):
        print("register")
        

class Stu(User):

    def enroll(self):
        print("enroll")
        
    def review(self):
        print("review")


class Phone:
    
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

class SmartPhone(Phone):

    pass