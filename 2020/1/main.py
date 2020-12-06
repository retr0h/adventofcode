import functools
import itertools

TARGET = 2020
RANGE = 3


with open("input", "r") as f:
    numbers = [int(n) for n in f]

    #
    # Trashed the original part 1 solution
    #
    #  HALF_THE_TARGET = TARGET // 2
    #  # filter values greater than 1/2 the target
    #  set1 = {n for n in numbers if n > HALF_THE_TARGET}
    #  # subtract remaining numbers from the target
    #  set2 = {(TARGET - n) for n in numbers if n <= HALF_THE_TARGET}

    #  union = set1 & set2
    #  for n in union:
    #      one = TARGET - n
    #      two = n
    #      print(one * two)

    permutations = itertools.permutations(numbers, RANGE)
    for pair in permutations:
        if sum(pair) == TARGET:
            result = functools.reduce((lambda x, y: x * y), pair)
            print(f"Answer: {result}")
            break
