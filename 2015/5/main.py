import re


def has_three_vowels(string):
    return re.search(r'([aeiou].*){3,}', string)


def has_consecutive_letters(string):
    return re.search(r'([a-z])\1', string)


def has_alternating_pairs(string):
    return re.search(r'([a-z])[a-z]\1', string)


def has_non_overlapping_pairs(string):
    return re.search(r'([a-z][a-z]).*\1', string)


def has_naughty_letters(string):
    return re.search(r'ab|cd|pq|xy', line)


def nice_string(string):
    return (has_three_vowels(string) and has_consecutive_letters(string) and
            not has_naughty_letters(string))


def new_nice_string(string):
    return (has_non_overlapping_pairs(string) and
            has_alternating_pairs(string))

with open('input', 'r') as f:
    lines = f.read().splitlines()
    nice = [line for line in lines if nice_string(line)]
    new_nice = [line for line in lines if new_nice_string(line)]

    print 'nice: {0}'.format(len(nice))
    assert 255 == len(nice)

    print 'new nice: {0}'.format(len(new_nice))
    assert 55 == len(new_nice)
