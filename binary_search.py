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
        binary_search(array, key, start, split)
    else:
        binary_search(array, key, split, end)
