"""
def find_secret_code(filename):
    with open(filename, 'r') as file:
        total_sum = 0
        for line in file:
            numbers = line.split()
            if numbers:  # check if the line is not empty
                first_number = int(numbers[0])
                last_number = int(numbers[-1])
                two_digit_number = int(str(first_number) + str(last_number))
                total_sum += two_digit_number
    return total_sum

# Use the function
filename = "input.txt"
print(find_secret_code(filename))

"""

"""
def find_secret_code(s):
    numbers = [int(i) for i in s if i.isdigit()]
    if len(numbers) >= 2:
        first_number = numbers[0]
        last_number = numbers[-1]
        two_digit_number = int(str(first_number) + str(last_number))
        return two_digit_number
    else:
        return "The string must contain at least two numbers."

# Use the function
s = "eightthree8fiveqjgsdzgnnineeight"
print(find_secret_code(s))

"""

"""
def find_secret_code(filename):
    with open(filename, 'r') as file:
        total_sum = 0
        for line in file:
            numbers = line.split()
            if numbers:  # check if the line is not empty
                first_number_str = ''.join(filter(str.isdigit, numbers[0]))
                last_number_str = ''.join(filter(str.isdigit, numbers[-1]))
                if first_number_str and last_number_str:  # check if the strings are not empty
                    first_number = int(first_number_str)
                    last_number = int(last_number_str)
                    two_digit_number = int(str(first_number) + str(last_number))
                    total_sum += two_digit_number
    return total_sum

# Use the function
filename = "input.txt"
print(find_secret_code(filename))

"""
"""
def find_secret_code(filename):
    with open(filename, 'r') as file:
        total_sum = 0
        for line in file:
            numbers = [word for word in line.split() if any(char.isdigit() for char in word)]
            if numbers:  # check if the line is not empty
                first_number_str = ''.join(filter(str.isdigit, numbers[0]))
                last_number_str = ''.join(filter(str.isdigit, numbers[-1])) if len(numbers) > 1 else first_number_str
                first_number = int(first_number_str)
                last_number = int(last_number_str)
                two_digit_number = int(str(first_number) + str(last_number))
                total_sum += two_digit_number
    return total_sum

# Use the function
filename = "input.txt"
print(find_secret_code(filename))
"""


import re

def sum_two_digit_numbers(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    total = 0
    for line in lines:
        digits = re.findall(r'\d', line)
        if len(digits) >= 2:
            two_digit_number = int(digits[0] + digits[-1])
        elif len(digits) == 1:
            two_digit_number = int(digits[0] + digits[0])
        else:
            continue
        #Display Numbers
        #print(f"Two-digit number formed: {two_digit_number}")
        total += two_digit_number
    return total

file_path = 'input.txt'
print(f"Sum: {sum_two_digit_numbers(file_path)}")

