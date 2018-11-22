
def fib(n):
    if n <= 1:
        return n
    fib_seq = list()
    fib_seq.append(0)
    fib_seq.append(1)
    for i in range(2, n + 1):
        a = fib_seq[i-1] + fib_seq[i-2]
        fib_seq.append(a)
    return fib_seq[-1]


def main():
    n = int(input().strip())
    print(fib(n))

if __name__ == '__main__':
     main()
