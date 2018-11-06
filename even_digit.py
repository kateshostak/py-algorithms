import random


def find_min_even_number_digit(n):
    min_digit = 10
    while n > 0:
        tmp_digit = n % 10
        if tmp_digit % 2 == 0:
            if tmp_digit < min_digit:
                min_digit = tmp_digit
        n = n//10
    if min_digit == 10:
        return None
    else:
        return min_digit


def main():
    n = random.randint(0, 9999999999)
    print(find_min_even_number_digit(n))


if __name__ == '__main__':
    main()
