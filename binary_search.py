def binary_search(array, key, start, end):
    if end - start == 1:
        if key == array[start]:
            return start
        elif key == array[end]:
            return end
        else:
            print('No such element in the array')
            return None

    split = (end + start)//2
    if key < array[split]:
        res = binary_search(array, key, start, split)
    else:
        res = binary_search(array, key, split, end)

    return res


def main():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(arr, 0, 0, len(arr) - 1))

if __name__ == '__main__':
    main()
