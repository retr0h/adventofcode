def get_fuel_requirements(mass):
    val = get_fuel_requirement(mass)
    if val > 0:
        return val + get_fuel_requirements(val)

    return 0


def get_fuel_requirement(mass):
    val = mass / 3
    val = int(val)  # round down
    val = val - 2

    return val


# Part 1
# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
assert 2 == get_fuel_requirement(12)
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
assert 2 == get_fuel_requirement(14)
# For a mass of 1969, the fuel required is 654.
assert 654 == get_fuel_requirement(1969)
# For a mass of 100756, the fuel required is 33583
assert 33583 == get_fuel_requirement(100756)


# Part 1
# The Fuel Counter-Upper needs to know the total fuel requirement.
# To find it, individually calculate the fuel needed for the mass
# of each module (your puzzle input), then add together all the
# fuel values.
with open('input', 'r') as f:
    masses = f.read().splitlines()
    r = [get_fuel_requirement(int(mass)) for mass in masses]
    print(sum(r))


# Part 2
# A module of mass 14 requires 2 fuel. This fuel requires no further fuel
# (2 divided by 3 and rounded down is 0, which would call for a negative fuel),
# so the total fuel required is still just 2.
assert 2 == get_fuel_requirements(12)
# At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires
# 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires
# 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total
# fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
assert 966 == get_fuel_requirements(1969)
# The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192
# + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
assert 50346 == get_fuel_requirements(100756)


# Part 2
# What is the sum of the fuel requirements for all of the modules on your spacecraft
# when also taking into account the mass of the added fuel? (Calculate the fuel
# requirements for each module separately, then add them all up at the end.)
with open('input', 'r') as f:
    masses = f.read().splitlines()
    r = [get_fuel_requirements(int(mass)) for mass in masses]
    print(sum(r))
