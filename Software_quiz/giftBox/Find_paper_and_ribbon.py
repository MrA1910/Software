def calculate_paper_and_ribbon(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    total_paper = 0
    total_ribbon = 0

    for line in lines:
        l, w, h = map(int, line.strip().split('x'))

        # Calculate the size of the gift wrapping paper
        sides = [l * w, w * h, h * l]
        paper = 2 * sum(sides) + min(sides)
        total_paper += paper

        # Calculate the length of the ribbon
        perimeters = [2 * (l + w), 2 * (w + h), 2 * (h + l)]
        ribbon = min(perimeters) + l * w * h
        total_ribbon += ribbon

    return total_paper, total_ribbon


# Use the function
paper, ribbon = calculate_paper_and_ribbon('input.txt')
print(f"Total size of gift wrapping paper: {paper} square units")
print(f"Total length of ribbon: {ribbon} units")
