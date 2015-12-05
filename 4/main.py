import sys
import hashlib

with open('input', 'r') as f:
    secret = f.read().strip()


def number_generator():
    for x in xrange(sys.maxint):
        yield x


def get_lowest_number(padding='00000'):
    for n in number_generator():
        md5 = hashlib.md5(secret + str(n)).hexdigest()
        if md5.startswith(padding):
            return n


num = get_lowest_number()
print 'padded with 5 zeros: {0}'.format(num)
assert 254575 == num

num = get_lowest_number('000000')
print 'padded with 6 zeros: {0}'.format(num)
assert 1038736 == num
