def insertion_sort(arr, end):
    if end == 0:
        return arr[end]

    end -= 1
    insertion_sort(arr, end)

    key = arr[end]
    i = end - 1
    while i >= 0 and arr[i] > key:
        arr[i+1] = arr[i]
        i -= 1

    arr[i+1] = key

    return arr


def main():
    my_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 77, 0]
    print(insertion_sort(my_arr, len(my_arr)))

if __name__ == '__main__':
    main()
