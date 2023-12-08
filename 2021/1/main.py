increases = 0

with open('input', 'r') as f:
    lines = f.readlines()
    measurements = [int(depth.strip()) for depth in lines]

    prev_depth = measurements[0]
    for depth in measurements[1:]:
        if depth > prev_depth:
            increases += 1
        prev_depth = depth


    print(increases)
