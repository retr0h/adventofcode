def get_increases(measurements):
    prev_depth = measurements[0]
    increases = 0

    for depth in measurements[1:]:
        if depth > prev_depth:
            increases += 1
        prev_depth = depth

    return increases


with open("input", "r") as f:
    lines = f.readlines()
    measurements = [int(depth.strip()) for depth in lines]

    ### A
    increases = get_increases(measurements)
    print(increases)

    ### B
    window_size = 3
    sliding_windows = [
        sum(measurements[i : i + window_size])
        for i in range(len(measurements) - window_size + 1)
    ]

    increases = get_increases(sliding_windows)
    print(increases)
