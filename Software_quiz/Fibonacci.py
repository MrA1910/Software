"""


def generate_odd_fibonacci(limit):
    a, b = 0, 1
    odd_sum = 0
    count = 0
    while count < limit:
        if a % 2 != 0:
            odd_sum += a
            count += 1
        a, b = b, a + b
    return odd_sum


# Calculate the sum of the first 100 odd Fibonacci numbers
odd_fibonacci_sum = generate_odd_fibonacci(100)
print(f"Sum of the first 100 odd Fibonacci numbers: {odd_fibonacci_sum}")

"""
"""
fib1, fib2 = 0, 1
odd_sum = 0

for _ in range(100):
    if fib1 % 2 != 0:
        odd_sum += fib1
    fib1, fib2 = fib2, fib1 + fib2

print("The sum of odd numbers in the first 100 Fibonacci numbers is:", odd_sum)
"""

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


def sum_of_odd_numbers_in_sequence(sequence):
    return sum(num for num in sequence if num % 2 != 0)


fib_sequence = fibonacci(100)
sum_of_odds = sum_of_odd_numbers_in_sequence(fib_sequence)

print("The sum of odd numbers in the first 100 Fibonacci numbers is:", sum_of_odds)
