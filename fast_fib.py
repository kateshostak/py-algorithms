def fib_decorator(func, n):
    def fib_saver():
        fib_seq = list()
        a = func(n)
        fib_seq.append(a)
        return fib_seq

    return fib_saver


def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


def main():
    n = int(input().strip())
    res = fib_decorator(fib, n)
    print(res())

if __name__ == '__main__':
     main()
