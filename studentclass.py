from person import Person 
class Student(Person):
    #constructor
    def __init__(self,sname,sage,year):
        super().__init__(sname,sage)
        self.academic_year = year
#    def say_hi(self):
#        return f"Hello {self.name} as student"
        
    