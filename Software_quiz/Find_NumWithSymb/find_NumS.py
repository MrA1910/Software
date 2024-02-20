import re

def sum_numbers_in_vicinity(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]

    symbols = {'+', '*', '/', '#', '@', '$', '%', '&', '-'}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    total_sum = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if re.match(r'\d+', ''.join(grid[i][j:j+3])):
                number_str = ''.join(grid[i][j:j+3])
                if number_str.isdigit():
                    number = int(number_str)
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[i]) and grid[nx][ny] in symbols:
                            print(f"Number {number} at position ({i}, {j}) has a symbol in its vicinity.")
                            total_sum += number
                            break

    return total_sum

print(sum_numbers_in_vicinity('input.txt'))
