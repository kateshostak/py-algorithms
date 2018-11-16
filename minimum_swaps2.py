def find_min(slice):
    min_elem = slice[0]
    min_i = 0
    for i in range(len(slice)):
        if slice[i] < min_elem:
            min_elem = slice[i]
            min_i = i
    return min_i, min_elem


def minimumSwaps(arr):
    swaps = 0
    for i in range(len(arr) - 1):
        j, elem = find_min(arr[i:])
        if elem != arr[i]:
            arr[i], arr[j+i] = arr[j+i], arr[i]
            swaps += 1
    print(arr)
    return swaps


if __name__ == '__main__':
    arr = [7, 1, 3, 2, 4, 5, 6]
    res = minimumSwaps(arr)
    print(res)
