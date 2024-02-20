# Calculate 2^1337
result = 2**1337

# Convert the result to a string to sum its digits
result_str = str(result)

# Sum the digits
digit_sum = sum(int(digit) for digit in result_str)

print("The sum of the digits of 2^1337 is:", digit_sum)
