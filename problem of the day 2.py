def sum_num(nums, target):
    s = set()
    for num in nums:
        c = target - num
        if c in s:
            return num, c
        s.add(num)
    return None


input_numbers = input("Enter a list of numbers : ").split()
nums = [int(num) for num in input_numbers]
target = int(input("Enter the target : "))


result = sum_num(nums, target)


if result:
    num1, num2 = result
    print(f"A pair of numbers that add up to {target} are: {num1} and {num2}")
else:
    print("No such pair of numbers in the list add up to the target .")