from heap import *
import random

def generate_arr(arr_length):
    arr = list()
    for i in range(arr_length):
        arr.append(random.randint(0, 100))
    return arr

def is_heap(arr):
    for i in range(len(arr)//2 + 1):
        left_i = 2 * (i + 1) - 1
        right_i = 2 * (i + 1)
        if left_i <= len(arr) - 1 and arr[i] < arr[left_i] or right_i <= len(arr) - 1 and arr[i] < arr[right_i]:
            return False
    return True

def main():
    arr_length = random.randint(10, 50)
    my_arr = generate_arr(arr_length)
    my_heap = Heap(my_arr)
    my_heap.print_heap()
    if is_heap(my_heap.heap):
        print('The given array is a heap')
    else:
        print('The given array is not a heap')

if __name__ == '__main__':
    main()