import math

class Heap():

    def __init__(self, arr):
        # self.length = len(arr)
        self.heap = self.make_heap(arr)

    def __iter__(self):
        return iter(self.heap)

    def __next__(self):
        next(iter(self.heap))

    def __getitem__(self, index):
        return self.heap[index]

    def __setitem__(self, index, value):
        self.heap[index] = value

    def __len__(self):
        return len(self.heap)

    def pop(self):
        self.heap.pop()

    def __str__(self):
        return str(self.heap)

    def parent(self, i):
        return math.floor(i/2) - 1

    def left(self, i):
        return 2*(i+1) - 1

    def right(self, i):
        return 2*(i+1)

    def make_heap(self, arr):
        length = len(arr)
        for i in range(length//2, -1, -1):
            self.max_heapify(arr, i)
        return arr

    def max_heapify(self, arr, i):
        if arr:
            length = len(arr)
            left = self.left(i)
            right = self.right(i)

            if i > length//2:
                return

            if left < length and arr[left] > arr[i]:
                largest = left
            else:
                largest = i

            if  right < length and arr[right] > arr[largest]:
                largest = right

            arr[i], arr[largest] = arr[largest], arr[i]

            if largest != i:
                self.max_heapify(arr, largest)


    def print_heap(self):
        print(self.heap)

    def is_empty(self):
        return not(self.heap)

    def max_elem(self):
        return self.heap[0]


def main():
    # my_arr = [500, 23, 56, 57, 478, 479, 900]
    my_arr = [1]
    my_heap = Heap(my_arr)
    my_heap.print_heap()


if __name__ == '__main__':
    main()