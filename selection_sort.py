def find_min(array):
    min_elem = array[0]
    for elem in array:
        if elem < min_elem:
            min_elem = elem
    return min_elem


def selection_sort(array):
    for i, elem in enumerate(array[1:], 1):
        min_elem = find_min(array[i:])
        array[i - 1], array[array[i:].index(min_elem) + i] = min_elem, array[i - 1]
    return array


def main():
    a = [0, 9, 8, 7, 0, 1]
    print(selection_sort(a))

if __name__ == "__main__":
    main()
