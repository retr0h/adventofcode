with open("input", "r") as f:
    totals = [
        sum(int(calorie) for calorie in group.split())
        for group in f.read().split("\n\n")
    ]

    totals.sort()

    ### A
    print(totals[-1])

    ### B
    print(sum(totals[-3:]))
