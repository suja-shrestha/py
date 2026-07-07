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

def is_even_or_odd(num):
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

is_even_or_odd(provided_number)

def break_and_continue_example(provided_number):
    for i in range(1, provided_number + 1):
        if i == 5:
            print("Breaking the loop at 5")
            break
        if i % 2 == 0:
            print(f"Skipping even number: {i}")
            continue
        print(f"Processing number: {i}")

break_and_continue_example(provided_number)

