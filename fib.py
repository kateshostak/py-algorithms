def fib(n):
    if n == 0:
        yield 0
    elif n == 1:
        yield 1
    yield fib(n - 1) + fib(n - 2)


def main():
    n = 7
    print(list(fib(n)))

if __name__ == '__main__':
    main()
