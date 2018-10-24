import generate_random_arr


def bublesort(arr):
    swapped = False
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            return arr
    return arr


def main():
    arr = generate_random_arr.generate_arr(0, 9, 0, 100)
    print(arr)
    print(bublesort(arr))

if __name__ == '__main__':
    main()
