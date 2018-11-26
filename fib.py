def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    n = 100
    print(list(fib(n)))

if __name__ == '__main__':
    main()
