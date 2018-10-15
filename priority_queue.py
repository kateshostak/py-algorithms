import heap

class PriorityQueue():
    def __init__(self, arr):
        self.heap = heap.Heap(arr)

    def heap_max(self):
        return self.heap[0]

    def heap_extract_max(self):
        if self.heap.is_empty():
            print('The heap is empty')
            return None
        else:
            max_elem = self.heap[0]
            print(max_elem)
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.heap.max_heapify(self.heap, 0)
            return max_elem

    def heap_increase_key(self, i, value):
        if value < self.heap[i]:
            print('New value must be bigger than the current value')
        else:
            self.heap[i] = value

    def increase_key(self):
        pass

def main():
    my_arr = [500, 23, 56, 57, 478, 479, 900]
    my_queue = PriorityQueue(my_arr)
    for i in range(8):
        my_queue.heap_extract_max()

if __name__ == '__main__':
    main()