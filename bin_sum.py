import random


def convert_to_list(n, align):
    return list(map(int, '{:0>11}'.format(n)))


def convert_to_bin(a, b):
    a_bin = f'{a:b}'
    b_bin = f'{b:b}'
    align = max(len(a_bin), len(b_bin)) + 1
    return convert_to_list(a_bin, align), convert_to_list(b_bin, align)


def bin_sum(a, b):
    a_bin, b_bin = convert_to_bin(a, b)
    c_bin = list()
    carry = 0
    for i in range(len(a_bin) - 1, -1, -1):
        c_i = (carry + a_bin[i] + b_bin[i]) % 2
        c_bin.append(c_i)
        if a_bin[i] == 0:
            carry = b_bin[i] and carry
        else:
            carry = b_bin[i] or carry
    return c_bin[-1::-1]


def main():
    a = random.randint(0, 1000)
    b = random.randint(0, 100)
    c = ''.join(map(str, bin_sum(a, b)))
    print(c)

if __name__ == '__main__':
    main()
