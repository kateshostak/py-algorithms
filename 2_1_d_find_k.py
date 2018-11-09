import time
from merge_sort import merge_sort
from insertion_sort import insertion_sort
from generate_random_arr import generate_arr


def measure_runtime(alg, arr):
    if alg == 'merge':
        start_time = time.time()
        merge_sort(arr, 0, len(arr))
        res = time.time() - start_time
    elif alg == 'insert':
        start_time = time.time()
        insertion_sort(arr)
        res = time.time() - start_time

    return res


def find_k(arr):
    merge_sort_time = measure_runtime('merge', arr)
    insertion_sort_time = measure_runtime('insert', arr)
    if insertion_sort_time <= merge_sort_time:
        return True
    else:
        return False


def main():
    res = 0
    number_of_tests = 90000000
    flag = True
    i = 2
    for _ in range(number_of_tests):
        while flag:
            arr = generate_arr(i, i, 0, 100)
            i += 1
            if not find_k(arr):
                flag = False
        res += i - 1

    print(res//number_of_tests)

if __name__ == '__main__':
    main()
