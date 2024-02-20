"""
def calculate_sum_of_powers():
    # Calculate the sum of powers from 2^2 to 2^100
    sum_2_to_100 = sum(2 ** i for i in range(2, 101))

    # Calculate the sum of powers from 100^2 to 100^100
    sum_100_to_100 = sum(i ** i for i in range(100, 101))

    # Add the two sums together
    total_sum = sum_2_to_100 + sum_100_to_100

    return total_sum

def convert_to_readable(number):
    # Convert the number to scientific notation
    formatted_number = f"{number:.2e}"

    # Extract the coefficient and exponent
    coefficient, exponent = formatted_number.split("e+")
    coefficient = float(coefficient)

    # Create a more human-readable representation
    readable_result = f"{coefficient:.2f} × 10^{exponent}"
    return readable_result

result = calculate_sum_of_powers()
result_readable = convert_to_readable(result)

print(f"The combined sum of powers from 2^2 to 100^100 is approximately {result_readable}.")

"""



def calculate_sum_of_powers():
    # Calculate the sum of powers from 2^2 to 2^100
    sum_2_to_100 = sum(2 ** i for i in range(2, 101))

    # Calculate the sum of powers from 100^2 to 100^100
    sum_100_to_100 = sum(i ** i for i in range(100, 101))

    # Add the two sums together
    total_sum = sum_2_to_100 + sum_100_to_100

    return total_sum


result = calculate_sum_of_powers()


print(result)
