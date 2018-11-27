def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
