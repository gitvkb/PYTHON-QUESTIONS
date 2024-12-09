num = 1  # Start with the number 1

while num <= 10:
    if num % 2 == 0:  # Check if the number is even
        print(f"Cube of {num}: {num ** 3}")
    else:  # If the number is odd
        print(f"Square of {num}: {num ** 2}")
    
    num += 1  # Increment the number
