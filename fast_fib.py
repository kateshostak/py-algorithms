def fib(n):
    if n <= 1:
        return n
    fib_1 = 0
    fib_2 = 1
    for i in range(n):
        fib_1, fib_2 = fib_1 + fib_2, fib_1

    return fib_1


def main():
    n = int(input().strip())
    print(fib(n))
if __name__ == '__main__':
     main()
