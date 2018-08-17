def merge_sort(arr, i, j):
    if j - i == 1:
        return

    m = (j + i) // 2

    merge_sort(arr, i, m)
    merge_sort(arr, m, j)

    merge(arr, i, m, j)

    return arr


def merge(arr, i, m, j):
    result = []

    s1, s2 = i, m
    while s1 < m and s2 < j:
        e1, e2 = arr[s1], arr[s2]
        if e1 < e2:
            result.append(e1)
            s1 += 1
        else:
            result.append(e2)
            s2 += 1

    while s1 < m:
        e1 = arr[s1]
        result.append(e1)
        s1 += 1

    while s2 < j:
        e2 = arr[s2]
        result.append(e2)
        s2 += 1

    for k in range(i, j):
        arr[k] = result[k - i]
