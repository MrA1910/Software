def count_houses_visited(filename):
    with open(filename, 'r') as file:
        directions = file.read()

    # Initialize the starting position and visited houses set
    x, y = 0, 0
    visited_houses = {(x, y)}

    # Define the movements for each direction
    moves = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}

    for direction in directions:
        if direction in moves:
            dx, dy = moves[direction]
            x, y = x + dx, y + dy
            visited_houses.add((x, y))

    return len(visited_houses)


print(count_houses_visited('input.txt'))
