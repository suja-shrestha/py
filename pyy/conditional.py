provided_number = int(input("Enter a number to check Composite/Prime or odd/even: "))

if provided_number <= 1:
    print(f"{provided_number} is neither prime nor composite.")
else:
    for i in range(2, provided_number):
        if provided_number % i == 0:
            print(f"{provided_number} is a composite number.")
            break
    else:
        print(f"{provided_number} is a prime number.")


if provided_number % 2 == 0:
    print(f"{provided_number} is an even number.")  
else:
    print(f"{provided_number} is an odd number.")   