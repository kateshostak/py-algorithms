def make_compare_p(desc):
    if desc:
        return lambda x, y: x < y

    return lambda x, y: x > y


def insertion_sort(array, desc=True):
    compare_p = make_compare_p(desc)
    for i, elem in enumerate(array[1:]):
        while i >= 0 and compare_p(array[i], elem):
            array[i+1] = array[i]
            i -= 1
        array[i+1] = elem

    return array
