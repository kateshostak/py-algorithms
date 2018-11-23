def fib_mod(n, m):
    if n <= 1:
        return n % m
    fib_seq = list()
    fib_seq.append(0)
    fib_seq.append(1)
    i = 2
    period = 0
    while period == 0 and i <= n:
        a = fib_seq[i-1]%m + fib_seq[i-2]%m
        fib_seq.append(a%m)
        if a%m == 0 and fib_seq[i-1] == 1:
            period = i
            return fib_seq[n%period]
        i += 1

    return fib_seq[-1]%m


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
