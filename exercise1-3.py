# Exercise 1: Factors

# Find all the factors of x using a loop and the operator %
# % means find remainder, for example 10 % 2 = 0; 10 % 3 = 1
x = 52633
for i in range(2, x):
    if x % i == 0:
        print(i)

#Exercise 2: Function
#Encapsulate the logic in a function:
# Write a function that prints all factors of the given parameter x

def print_factor(x):
    # your code here
    for i in range(2, x):
        if x % i == 0:
            print(i)

# Exercise 3: List Iteration
# Apply the function to a list:
# Write a program to find all factors of the numbers in the list l

l = [52633, 8137, 1024, 999]
# your code here
for number in l:
    print(f"Factors of {number}:")
    print_factor(number)