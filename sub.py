import pdb


def max_subarr(arr):
    tmp_sum = max_sum = arr[0]
    start = tmp_start = end = 0
    for i in range(1, len(arr)):
        if tmp_sum + arr[i] < arr[i]:
            tmp_start = i
            tmp_sum = arr[i]
        else:
            tmp_sum += arr[i]
        if tmp_sum > max_sum:
            max_sum = tmp_sum
            end = i
            start = tmp_start
    return start, end, max_sum


def main():
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(max_subarr(arr))

if __name__ == '__main__':
    main()
