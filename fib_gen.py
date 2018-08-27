def fib(n):
    fib_1, fib_2 = 0, 1
    for _ in range(n):
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1 + fib_2


def main():
    n = 7
    print(list(fib(n)))

if __name__ == '__main__':
    main()
