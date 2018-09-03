import random
import time

import max_subarray_recursive
import max_subarray_n2


def generate_array(n):
    random.seed(1)
    return list(random.randint(-100, 100) for _ in range(n))

def get_running_time(alg, arr):
    start_time = time.time()
    alg.max_subarray(arr)
    return time.time() - start_time

def compare_algorithms():
    i = 2

    while True:
        arr = generate_array(i)

        bruteforce_alg_time = get_running_time(max_subarray_n2, arr)
        recursive_alg_time = get_running_time(max_subarray_recursive, arr)

        if bruteforce_alg_time > recursive_alg_time:
            break
        i += 1

    return i

def main():
    arr_len = 0
    for i in range(50):
        arr_len += compare_algorithms()

    print(f'The recursive subarray algorithm outrans the bruteforce algorithm since array length is >= {arr_len//i}')


if __name__ == '__main__':
    main()
