total = 0
ribbon = 0
with open('input', 'r') as f:
    for line in f.read().splitlines():
        length, width, height = list(map(int, line.split('x')))

        side1 = length * width
        ribbon1 = length + length + width + width
        side2 = width * height
        ribbon2 = width + width + height + height
        side3 = height * length
        ribbon3 = height + height + length + length
        bow = length * width * height

        ribbon += bow + min(ribbon1, ribbon2, ribbon3)
        total += 2 * side1 + 2 * side2 + 2 * side3 + min(side1, side2, side3)

print 'paper: {0}'.format(total)
assert 1606483 == total

print 'ribbon: {0}'.format(ribbon)
assert 3842356 == ribbon
