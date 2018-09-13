import random
import math

def random_bin():
    return random.randint(0,1)

def random_int(a, b):
    n = math.floor(math.log2(b - a)) + 1
    tmp_bin = str()
    for _ in range(n):
        tmp_bin += str(random_bin())

    c = int(tmp_bin, 2)
    if c <= (b - a):
        return c + a
    else:
        return random_int(a, b)

def main():
    a, b = 1, 2
    print(random_int(a, b))

if __name__ == '__main__':
    main()
