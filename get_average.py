numbers = []

while True: 
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
            break
    
average = sum(numbers) / len(numbers)
print(average)