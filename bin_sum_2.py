import itertools
import random


def bin2int(a):
    return int("".join(map(str, a)), 2)


def int2bin(i):
    return list(map(int, bin(i).replace("0b", "")))


def carry_sum(ai, bi, carry):
    return (ai + bi + carry) % 2, (ai + bi + carry) // 2


def bin_sum(a, b):
    c, carry = [], 0

    for ai, bi in itertools.zip_longest(reversed(a), reversed(b), fillvalue=0):
        ci, carry = carry_sum(ai, bi, carry)
        c.append(ci)

    if carry != 0:
        c.append(carry)
 
    return list(reversed(c))


def main():
    for i in range(0, 10000):
        a, b = random.randint(0, 100000), random.randint(0, 100000)
        c = a + b

        a_bin, b_bin = int2bin(a), int2bin(b)
        c_bin = bin_sum(a_bin, b_bin)

        if c != bin2int(c_bin):
            print("a = %s, b = %s, c = %s, c_bin = %s" % (a, b, c, bin2int(c_bin)))


if __name__ == '__main__':
    main()
