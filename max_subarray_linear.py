def max_subarray(arr):
    max_ending_here = max_so_far = arr[0]
    for elem in arr[1:]:
        print(f'max_ending_here::{max_ending_here}::max_so_far::{max_so_far}')
        max_ending_here = max(elem, max_ending_here + elem)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def main():
    arr = [13, -3, -25, 20, -3, -16, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(max_subarray(arr))


if __name__ == '__main__':
    main()