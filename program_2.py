'''Random Number File Writer Program
By Grace LeVoir
3 - 27 - 26'''


# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

import random

number_of_numbers = int(input('How many numbers do you want (up to 1000)? '))
number_file = open('number_file.txt', 'w')

for i in range(number_of_numbers):

    number = str(random.randint(1, 500))
    number_file.write(f'{number}\n')

number_file.close()