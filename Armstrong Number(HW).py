# Armstrong Number Checker
# Take input from user
num = int(input("Enter a number: "))

# Convert number to string to count digits
num_str = str(num)
power = len(num_str)

# Calculate sum of digits raised to 'power'
total = 0
for digit in num_str:
    total += int(digit) ** power

# Check result
if total == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is NOT an Armstrong number.")