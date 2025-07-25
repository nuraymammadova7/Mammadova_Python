numbers = [int(num) for num in input("Enter numbers separated by space: ").split()]
for num in numbers:
    if num % 3 == 0:
        print(num)