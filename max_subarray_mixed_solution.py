import time


def max_left_sum(start, middle, arr):
    max_sum = tmp_sum = 0
    max_sum_i = 0
    for i in range(middle, start - 1, -1):
        tmp_sum += arr[i]
        if tmp_sum > max_sum:
            max_sum = tmp_sum
            max_sum_i = i

    return max_sum_i, max_sum


def max_right_sum(middle, end, arr):
    max_sum = tmp_sum = 0
    max_sum_i = 0
    for i in range(middle, end + 1):
        tmp_sum += arr[i]
        if tmp_sum > max_sum:
            max_sum = tmp_sum
            max_sum_i = i

    return max_sum_i, max_sum


def find_cross_subarray(start, middle, end, arr):
    start, left_sum = max_left_sum(start, middle, arr)
    end, rigth_sum = max_right_sum(middle + 1, end, arr)
    return start, end, left_sum + rigth_sum


def bruteforce(arr):
    max_sum = tmp_sum = 0
    start = end = 0
    for i in range(len(arr)):
        tmp_sum = 0
        for j in range(i, len(arr)):
            tmp_sum += arr[j]
            if tmp_sum > max_sum:
                max_sum = tmp_sum
                max_sum_start = i
                max_sum_end = j

    return max_sum_start, max_sum_end, max_sum


def find_max_subarray(start, end, arr):
    if end <= 50:
        return bruteforce(arr)

    middle = (start + end)//2
    left_start, left_end, left_sum = find_max_subarray(start, middle, arr)
    rigth_start, right_end, rigth_sum = find_max_subarray(middle + 1, end, arr)
    cross_start, cross_end, cross_sum = find_cross_subarray(start, middle, end, arr)

    if left_sum >= rigth_sum and left_sum >= cross_sum:
        return left_start, left_end, left_sum
    elif rigth_sum >= left_sum and rigth_sum >= cross_sum:
        return rigth_start, right_end, rigth_sum
    else:
        return cross_start, cross_end, cross_sum


def main():
    arr = [13, -3, -25, 20, -3, -16, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    start = 0
    end = len(arr)
    print(find_max_subarray(start, end - 1, arr))

if __name__ == '__main__':
    main()
