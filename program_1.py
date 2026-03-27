'''Item Counter Program
By Grace LeVoir
3 - 27 - 26'''


# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    # Add your code here #

    name_series = open('names.txt','r')
    count = 0

    for name in name_series:
        count += 1

    name_series.close()

    ######################
    print(f'There are {count} names in the file')


# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()