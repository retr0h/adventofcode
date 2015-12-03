from collections import defaultdict

x = 0
y = 0
positions = defaultdict(int)
positions['0:0'] = 1

with open('input', 'r') as f:
    for instructions in f:
        for direction in list(instructions):
            if direction == '^':
                y += 1
            elif direction == 'v':
                y -= 1
            elif direction == '>':
                x += 1
            elif direction == '<':
                x -= 1
            key = '{}:{}'.format(x, y)
            positions[key] += 1

    print 'visited: {0}'.format(len(positions))
