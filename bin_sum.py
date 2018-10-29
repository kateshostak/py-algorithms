import generate_random_arr


def bin_sum(a, b):
    c = list()
    carry = 0
    for i in range(len(a) - 1, -1, -1):
        c_i = (carry + a[i] + b[i]) % 2
        c.append(c_i)
        if a[i] == 0:
            carry = b[i] and carry
        else:
            carry = b[i] or carry
    c.append(carry)
    return c[-1::-1]


def main():
    a = generate_random_arr.generate_arr(3, 3, 0, 1)
    b = generate_random_arr.generate_arr(3, 3, 0, 1)
    str_a = ''.join(map(str,a))
    str_b = ''.join(map(str,b))
    int_a = int(str_a, base=2)
    int_b = int(str_b, base=2)
    int_sum = int_a + int_b
    print(int_a, int_b, int_sum)
    c = bin_sum(a,b)
    print(c)
    c = ''.join(map(str, bin_sum(a, b)))
    print(int(c, base=2))

if __name__ == '__main__':
    main()
