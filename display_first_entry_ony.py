numbers = [float(input(f"Enter number {i + 1}: "))for i in range(10)]

unique_numbers = [num for num in numbers if numbers.count(num) == 1]
duplicate_numbers = [num for num in numbers if numbers.count(num) > 1]

print(unique_numbers, duplicate_numbers)