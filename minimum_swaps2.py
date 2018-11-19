def minimumSwaps(arr):
    swaps = 0
    i = 0
    while i < len(arr) - 1:
        if arr[i] != i + 1:
            j = arr[i] - 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
        else:
            i += 1
    return swaps


if __name__ == '__main__':
    arr = [7, 1, 3, 2, 4, 5, 6]
    res = minimumSwaps(arr)
    print(res)
