# Python program to check if a number is prime or not
#Take input from the user
num=int(input("Enter a number: "))
#Check if the number is greater than 1 (since prime number are > 1)
if num > 1:
    #Loop only up to the square root of the number for efficieny
    for i in range(2, int(num**0.5)+1):
        #If the number is divisible by any number, it's not prime number
        if (num % i) == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        #If no divisors were found, the number is prime
        print(f"{num} is a prime number.")
else:
    #Number less than 2 are not prime numbers.
    print(f"{num} is not a prime number. ")