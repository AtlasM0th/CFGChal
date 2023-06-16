# Import & define
import numpy as np
again = 'y'

# Introduce
print("Welcome to the array sorter!")

# Create the loop to sort more integers if the user wants to
while True:

    # Enter an input of up to 100 numbers
    numbers = input("Please enter your list of integers, seperated only by spaces: ")
    numbers = list(map(int, numbers.split()))

    if len(numbers) > 100:
        print("You have entered more than 100 integers. \n")
        continue

    # Convert string into array
    array = np.array(numbers)

    # Ask the user if they would like to sort L -> S or S -> L
    print("Please type choose if you would like to order smallest to largest, or largest to smallest")
    order = input("Small to large: 'S', large to small 'L': ")
    order = order.upper()

    # Sort the array
    if order == "L":
        numberSort = np.sort(array)[::-1]
    elif order == "S":
        numberSort = np.sort(array)
    else:
        print("Invalid input")
        continue

    # Print the sorted array
    print("Your array as is follows:  \n", numberSort)

    again = input("Please type 'y' to enter another array, anything else will exit you from the program: \n")
    again = again.lower()

    if again != 'y':
        break
