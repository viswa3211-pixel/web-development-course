# Python program to print a star pattern based on the number of rows specified by the user
#Get the number of rows from the user
n=int(input("Enter the number of rows: "))
#outer loop for each row
for i in range(1,n+1):
    #inner loop for each column in the row
    for j in range(i):
        #Print star, end with space instead of the new line
        print("*", end=" ")
    #After each row, print a new line
    print()
