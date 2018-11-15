def max_subarr(arr):

    max_arr = 0
    start = end = 0
    for i in range(len(arr)):
        tmp_arr = 0
        for j in range(i, len(arr)):
            tmp_arr += arr[j]
            if tmp_arr > max_arr:
                max_arr = tmp_arr
                start = i
                end = j
    return max_arr, start, end


def main():
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(max_subarr(arr))

if __name__ == '__main__':
    main()
