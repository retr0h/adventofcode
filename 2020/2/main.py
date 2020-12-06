def part_one_check_policy(policy, password):
    rule, letter = policy.split()
    low, high = list(map(int, rule.split("-")))

    occurrences = password.count(letter)
    if occurrences >= low and occurrences <= high:
        print(password)


def part_two_check_policy(policy, password):
    rule, letter = policy.split()
    pos0, pos1 = list(map(int, rule.split("-")))

    if (password[pos0 - 1] == letter) ^ (password[pos1 - 1] == letter):
        print(password)


with open("input", "r") as f:
    for line in f.read().splitlines():
        policy, password = [x.strip() for x in line.split(":")]
        # part_one_check_policy(policy, password)
        part_two_check_policy(policy, password)
