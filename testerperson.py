from person import Person
from stack import Stack

stack = Stack()

#1

add_guest(stack, Person("Ali",25,"99554444"))

#2
view_guests(stack)
remove_guest(stack)
view_guests(stack)

#3
get_guest_count(stack)