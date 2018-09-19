import random

def generate_matrix(n):
    return [[random.randint(0, 1) for i in range(n)] for j in range(n)]


def multiply_matrices(a, b):
    c = list()
    n = len(a)
    for i in range(n):
        tmp_row = list()
        for j in range(n):
            tmp_elem = 0
            for k in range(n):
                tmp_elem += a[i][k]*b[k][j]

            tmp_row.append(tmp_elem)

        c.append(tmp_row)
    return c

def main():
    n = 3
    a = generate_matrix(n)
    b = generate_matrix(n)
    print(multiply_matrices(a, b))


if __name__ == '__main__':
    main()