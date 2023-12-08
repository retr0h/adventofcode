import re


def has_three_vowels(string):
    return re.search(r'([aeiou].*){3,}', string)


def has_consecutive_letters(string):
    return re.search(r'([a-z])\1', string)


def has_naughty_letters(string):
    return re.search(r'ab|cd|pq|xy', line)


def nice_string(string):
    return (has_three_vowels(string) and
            has_consecutive_letters(string) and not
            has_naughty_letters(string))


nice = 0
naughty = 0
with open('input', 'r') as f:
    for line in f.read().splitlines():
        if nice_string(line):
            nice += 1
        else:
            naughty += 1

print 'nice: {0}'.format(nice)
assert nice == 255

print 'naughty: {0}'.format(naughty)
assert naughty == 745
