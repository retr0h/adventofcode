floor = 0
basement = False
with open('input') as f:
    for line in f:
        for index, l in enumerate(list(line), 1):
            if l == '(':
                floor += 1
            elif l == ')':
                floor -= 1

            if floor == -1 and basement is False:
                basement = True
                print index

print floor
