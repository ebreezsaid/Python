def oddEven(n):
    if n%2 == 0:
        return 'Even'
    else:
        return 'odd'

    
oddEven1 = lambda n:(n%2 and 'odd' or 'even')
print(oddEven1(14))
print(oddEven1(13))