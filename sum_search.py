from merge_sort import merge_sort


def find_pair(array, x):
    left_index = 0
    right_index = len(array) - 1
    while left_index < right_index:
        if array[left_index] + array[right_index] == x:
            return True
        elif array[left_index] + array[right_index] < x:
            left_index += 1
        else:
            right_index -= 1


def main():
    array = [10, 4, 5, 7, 1, 1]
    sorted_array = merge_sort(array, 0, len(array))
    x = 10
    if find_pair(sorted_array, x):
        print('The pair exists.')

if __name__ == '__main__':
    main()
