TREE = "#"
tree_count = 0

with open("input", "r") as f:
    data = [line.strip() * 50 for line in f.readlines()]

    x = 0
    for d in data:
        if TREE in d[x]:
            tree_count += 1
        x += 3

    print(tree_count)
