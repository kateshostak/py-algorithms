import math

class Heap():

    def __init__(self, arr):
        self.length = len(arr)
        self.heap = self.make_heap(arr)

    def parent(self, i):
        return math.floor(i/2) - 1

    def left(self, i):
        return 2*(i+1) - 1

    def right(self, i):
        return 2*(i+1)

    def make_heap(self, arr):
        for i in range(self.length//2, -1, -1):
            self.max_heapify(arr, i)
        return arr

    def max_heapify(self, arr, i):
        left = self.left(i)
        right = self.right(i)

        if i > self.length//2:
            return

        if left < self.length and arr[left] > arr[i]:
            largest = left
        else:
            largest = i

        if  right < self.length and arr[right] > arr[largest]:
            largest = right

        arr[i], arr[largest] = arr[largest], arr[i]

        if largest != i:
            self.max_heapify(arr, largest)


    def print_heap(self):
        print(self.heap)

def main():
    my_arr = [500, 23, 56, 57, 478, 479, 900]
    # my_arr = [23, 17, 14, 6, 13, 10, 1, 5, 7, 12]
    my_heap = Heap(my_arr)
    my_heap.print_heap()


if __name__ == '__main__':
    main()