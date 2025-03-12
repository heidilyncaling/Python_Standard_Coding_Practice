numbers = []

while True: 
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
            break
           
sorted_numbers = sorted(numbers, reverse=True)

print(sorted_numbers)