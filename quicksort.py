import generate_random_arr


def partition(arr, low, high):
    pivot = arr[-1]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quicksot(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksot(arr, low, p - 1)
        quicksot(arr, p, high)
    return arr



def main():
    arr = generate_random_arr.generate_arr(0, 9, 0, 100)
    print(arr)
    print(quicksot(arr, 0, len(arr) - 1))

if __name__ == '__main__':
    main()