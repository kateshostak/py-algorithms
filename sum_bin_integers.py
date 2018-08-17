def bin_sum(a, b):
    c = list()
    q = 0
    for i in range(len(a) - 1, -1, -1):
        temp_c = (a[i] + b[i] + q) % 2
        if a[i] and b[i]:
            q = 1
        elif (a[i] or b[i]) and q:
            q = 1
        else:
            q = 0

        c.append(temp_c)

    if q:
        c.append(q)
    return c[::-1]
