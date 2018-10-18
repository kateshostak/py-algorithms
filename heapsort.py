import heap


def heapsort(my_arr):
    sorted_arr = list()
    my_heap = heap.Heap(my_arr)
    while len(my_arr) > 2:
        sorted_arr.append(my_heap.heap[0])
        my_heap.heap[0] = my_heap.heap[-1]
        my_heap.heap.pop()
        my_heap.max_heapify(my_heap.heap, 0)

    if my_arr[0] > my_arr[1]:
        sorted_arr.append(my_arr[0])
        sorted_arr.append(my_arr[1])
    else:
        sorted_arr.append(my_arr[1])
        sorted_arr.append(my_arr[0])

    return sorted_arr[::-1]


def main():
    sorted_arr = list()
    my_arr = [100, 99, 97, 95, 89, 80, 92, 77, 68, 77, 80, 33, 59, 49, 90, 50, 25, 35, 61, 68, 60, 69, 78, 30, 22, 36, 58, 13, 0, 53, 4, 4, 34, 6, 23, 32, 31, 56, 5, 34, 5, 1, 51, 12, 66, 35, 50, 0, 5]
    print(heapsort(my_arr))

if __name__ == '__main__':
    main()
