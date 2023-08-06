from person import Person
from studentclass import Student
from techer import Techer
def main():
    Ibreez = Person("Ibreez AL-Aufi",21)
    person2 = Person("Said")
    
    std1 = Student("Sara",18,2021)
    std2 = Student("ali",24,2019)
    
    
    tec1=Techer("hamza",30,5)
    tec2=Techer("hanaa",40,8)
    
    print(person2.descrip())
    print(Ibreez.get_name())
    Ibreez.set_name("Ibreez Said")
    print(Ibreez.get_name())
    print(Ibreez.descrip())
    Ibreez.run()      
    Ibreez.laugh()
    person2.laugh()
    
    print(std1.say_hi())
    print(Student.say_hi(std2))
    std1.run() 
    
    print(tec1.say_hi())
    print(Student.say_hi(tec2))
    tec1.laugh()
    
    print(Ibreez.say_hi())
    print(Person.say_hi(person2))    
main()