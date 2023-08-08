def is_even(L):
    evenList = []
    for num in L :
        if num%2 == 0 : #even
            evenList.append(num)
    return evenList
numbers = [10,2,3,14,17,29,19,18,22,26]
even = is_even(numbers)
print("Numbers: " ,numbers)
print("even numbers: " ,even)

#using filter
evenusingfilter = list(filter(lambda n : n % 2 == 0 , numbers))
print("Filtered even: " ,evenusingfilter)