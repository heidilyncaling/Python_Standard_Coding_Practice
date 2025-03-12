numbers = []

while True: 
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
            break
           
sorted_numbers = sorted(numbers)

print(sorted_numbers)