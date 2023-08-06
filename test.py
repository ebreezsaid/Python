from person import Person
from techer import Techer
def main():
    p1 = Person("ahmed",24,1500)
    print(p1.descrip())
    print(p1.bouns())
    t = Techer("ali",40,1500,3)
    print(t.descrip())
    print(t.bouns())
main()