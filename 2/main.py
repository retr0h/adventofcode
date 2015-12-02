total = 0
with open('input', 'r') as f:
    for line in f.read().splitlines():
        length, width, height = list(map(int, line.split('x')))

        side1 = (length * width)
        side2 = (width * height)
        side3 = (height * length)

        total += 2 * side1 + 2 * side2 + 2 * side3 + min(side1, side2, side3)

print total
