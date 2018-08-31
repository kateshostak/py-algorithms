def max_subarray(arr):
    max_sum = 0
    max_sum_start = 0
    max_sum_end = 0
    tmp_sum = 0
    for i in range(len(arr)):
        tmp_sum = 0
        for j in range(i, len(arr)):
            tmp_sum += arr[j]
            if tmp_sum > max_sum:
                max_sum = tmp_sum

    return max_sum


def main():
    arr = [13, -3, -25, 20, -3, -16, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(max_subarray(arr))

if __name__ == '__main__':
    main()