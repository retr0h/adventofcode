n = 0
with open('input') as f:
    for line in f:
        for l in list(line):
            if l == '(':
                n = n + 1
            elif l == ')':
                n = n - 1

print n
