def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def count_triangles(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            sides = list(map(int, line.split()))
            if len(sides) != 3:
                print(f"Invalid data: {sides}")
                continue
            if is_triangle(*sides):
                count += 1
    return count


filename = "input.txt"
print(f"The number of valid triangles in the file is {count_triangles(filename)}")
