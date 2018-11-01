import random
from bin_sum import bin_sum


def convert_to_list(n):
    return list(map(int, '{:0>11}'.format(f'{n:b}')))


def test_bin_sum(a, b):
    c = a + b
    c_bin = convert_to_list(c)
    if c_bin == bin_sum(a, b):
        return True


def main():
    for i in range(50):
        a = random.randint(0, 1000)
        b = random.randint(0, 100)
        if not test_bin_sum(a, b):
            print(a, b)

if __name__ == '__main__':
    main()
