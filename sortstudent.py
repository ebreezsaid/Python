def insertion_sort_students(dic):
    for i in range(1, len(dic)):
        key = dic[i]
        j = i - 1
        while j >= 0 and key['gpa'] > dic[j]['gpa']:
            dic[j + 1] = dic[j]
            j -= 1
        dic[j + 1] = key

def main():
    students = [
        {"name": "Alice", "age": 20, "gpa": 3.9},
        {"name": "Bob", "age": 22, "gpa": 3.7},
        {"name": "Charlie", "age": 21, "gpa": 4.0},
        {"name": "David", "age": 19, "gpa": 3.5},
    ]


    print("Original dic:", students)
    insertion_sort_students(students)
    print("-----------------------------")
    print("Sorted dic")
    for dic in students:
        print(dic)
main()