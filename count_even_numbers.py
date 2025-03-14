numbers = [
    float(input(f"Enter number {i+1}: ")) for i in range(10)]

even = sum (1 for num in numbers if num%2 == 0)
print (even)