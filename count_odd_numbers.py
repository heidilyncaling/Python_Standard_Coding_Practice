numbers = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
odd_num = sum(1 for num in numbers if num % 2 != 0)
print("Number of odd numbers:", odd_num)
