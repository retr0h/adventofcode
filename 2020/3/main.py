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




    #  Right 1, down 1.
    #  Right 3, down 1. (This is the slope you already checked.)
    #  Right 5, down 1.
    #  Right 7, down 1.
    #  Right 1, down 2.

