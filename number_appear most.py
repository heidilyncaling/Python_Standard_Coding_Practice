numbers = []

while True: 
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
            break

if numbers:
     max_count = max(numbers.count(n) for n in numbers)
     most_frequent = sorted({n for n in numbers if numbers.count(n) == max_count})
     print(most_frequent)

else:
     print("No numbers entered.")