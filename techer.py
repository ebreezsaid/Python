from person import Person
class Techer(Person):
    #constructor
    def __init__(self,tname,tage,salary,year):
        super().__init__(tname,tage,salary)
        self.techeing_year = year
        
    def bouns(self):
        t = super().bouns() * 2
        return t
    
    def say_hi(self):
        print(super().say_hi())
        return f"Hello {self.name} as techer"    
    