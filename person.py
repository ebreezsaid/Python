class Person():
    #constructor to ceate object
    #initialize instance variable
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def bouns(self):
        b = self.salary * 0.005
        return b
    def say_hi(self):
        return f"Hello {self.name} as person"       
    #use term of encapsulation
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    #setter / mutotur methods
    def set_name(self,newName):
        self.name = newName
    def set_age(self,newAge) :
        self.age = newAge
    def run(self):
        print(self.name , "is running")
    def descrip(self):
        return f"Person name is {self.name} is {self.age} years old"
    def laugh(self):
        print(self.name ,"say hahahahaha")
        
