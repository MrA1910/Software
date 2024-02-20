"""
def calculate_prime_factors(N):
    prime_factors = set()
    if N % 2 == 0:
        prime_factors.add(2)
        while N % 2 == 0:
            N = N // 2
    for factor in range(3, N + 1, 2):
        if N % factor == 0:
            prime_factors.add(factor)
            while N % factor == 0:
                N = N // factor
    return prime_factors


input_number = 87492774
output = calculate_prime_factors(input_number)
print(f"Prime factors of {input_number} are {output}")
"""

""""
def prime_fac(num):
    a = num
    pf = []
    for x in range(2, a + 1):
        while a % x == 0:
            pf.append(x)
            a = a // x
    if a == 1:
        return pf


input_number = 87492774
output = prime_fac(input_number)
print(f"Prime factors of {input_number} are {output}")
"""

"""
def calculate_prime_factors(N):
    prime_factors = set()
    if N % 2 == 0:
        prime_factors.add(2)
        while N % 2 == 0:
            N = N // 2
    for factor in range(3, N + 1, 2):
        if N % factor == 0:
            prime_factors.add(factor)
            while N % factor == 0:
                N = N // factor
    return prime_factors


input_number = 87492774
output = calculate_prime_factors(input_number)
output_string = ', '.join(map(str, output))  # Convert factors to a comma-separated string
print(f"Prime factors of {input_number} are: {output_string}")
"""


def prime_fac(num):
    a = num
    pf = []
    for x in range(2, a + 1):
        while a % x == 0:
            pf.append(x)
            a = a // x
    if a == 1:
        return pf


input_number = 87492774         # or int(input("Numbers :"))
output = prime_fac(input_number)
output_string = ', '.join(map(str, output))  # Convert factors to a comma-separated string
print(f"Prime factors of {input_number} are: {output_string}")
