def open_file():
    with open('input', 'r') as f:
        return f.read()


def get_directions(instructions):
    x = 0
    y = 0
    current = (x, y)
    positions = set()
    positions.add(current)
    for direction in list(instructions):
        if direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1
        elif direction == '>':
            x += 1
        elif direction == '<':
            x -= 1
        current = (x, y)
        positions.add(current)
    return positions


instructions = open_file()
positions = get_directions(instructions)

print 'visited: {0}'.format(len(positions))
assert len(positions) == 2572

positions = get_directions(instructions[::2]) | get_directions(instructions[1::2])

print 'visited: {0}'.format(len(positions))
assert len(positions) == 2631
