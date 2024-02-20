import re


def sum_and_show_numbers_around_symbols(file_path):
    with open(file_path, 'r') as file:
        data = [re.findall(r'\d+|[^0-9]', line.strip()) for line in file.readlines()]

    symbols = ['+', '*', '/', '#', '@', '$', '%', '&', '-']
    total = 0
    numbers = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in symbols:
                # Check the eight directions around the symbol
                for dx, dy in [(-1, 0), (1, 0), (-2, 0), (2, 0), (-3, 0), (3, 0), (0, -1), (0, 1), (0, -2), (0, 2),
                               (0, -3), (0, 3), (-3, -1), (-3, 1), (3, -2), (3, 2), (3, -3), (3, 3)]:
                    nx, ny = i + dx, j + dy
                    # Check if the new position is inside the grid and is a digit
                    if 0 <= nx < len(data) and 0 <= ny < len(data[nx]) and data[nx][ny].isdigit():
                        num = int(data[nx][ny])
                        total += num
                        numbers.append(num)

    return total, numbers


total, numbers = sum_and_show_numbers_around_symbols('input.txt')
print(f"The total sum of the numbers is: {total}")
print(f"The numbers are: {numbers}")
