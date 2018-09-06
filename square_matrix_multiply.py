import random

def generate_matrix(n):
    return [[random.randint(-100, 100) for i in range(n)] for j in range(n)]


def multiply_matrices(a, b):
    c = list()
    for i in range(len(a)):
        tmp_elem = 0
        for j in range(i):
            tmp_elem += a[i][j]*b[j][i]
            c.append(tmp_elem)
    return c

def main():
    n = 5
    a = generate_matrix(n)
    b = generate_matrix(n)
    print(multiply_matrices(a, b))


if __name__ == '__main__':
    main()