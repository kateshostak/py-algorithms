def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 400 == 0 or year % 100 != 0:
            leap = True
    return leap

def main():
    years = [2400, 2000, 1800, 1900, 2100, 2200, 2300, 2500]
    for year in years:
        print(f'{year} :: {is_leap(year)}')

if __name__ == '__main__':
    main()