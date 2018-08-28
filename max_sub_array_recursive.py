def max_left_sum(middle, start, arr):
    max_sum = 0
    temp_sum = 0
    max_i = start
    for i in range(middle, start - 1, -1):
        print(arr[i])
        temp_sum += arr[i]
        if temp_sum > max_sum:
            max_sum = temp_sum
            max_i = i
    return max_i, max_sum


def max_right_sum(middle, end, arr):
    max_sum = 0
    temp_sum = 0
    max_i = middle
    for i in range(middle, end + 1):
        print(arr[i])
        temp_sum += arr[i]
        if temp_sum > max_sum:
            max_sum = temp_sum
            max_i = i
    return max_i, max_sum


def find_max_crossing_subarray(start, middle, end, arr):
    start, left_sum = max_left_sum(middle, start, arr)
    end, right_sum = max_right_sum(middle + 1, end, arr)
    cross_sum = left_sum + right_sum
    return start, end, cross_sum


def find_max_subarray(start, end, arr):
    if start == end:
        return start, end, arr[start]
    middle = (start + end)//2

    left_start, left_end, left_sum = find_max_subarray(start, middle, arr)
    right_start, right_end, right_sum = find_max_subarray(middle + 1, end, arr)
    cross_start, cross_end, cross_sum = find_max_crossing_subarray(start, middle, end, arr)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_start, left_end, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_start, right_end, right_sum
    else:
        return cross_start, cross_end, cross_sum


def main():
    arr = [13, -3, -25, 20, -3, -16, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    start = 0
    end = len(arr)
    print(find_max_subarray(start, end - 1, arr))


if __name__ == '__main__':
    main()
