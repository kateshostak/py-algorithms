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
            parent_i = self.heap.parent(i)
            while i > 0 and self.heap[parent_i] < value:
                self.heap[parent_i], self.heap[i] = self.heap[i], self.heap[parent_i]
                i = parent_i
                parent_i = self.heap.parent(i)

    def max_heap_insert(self, value):
        self.heap.heap.append(value)
        self.heap_increase_key(len(self.heap.heap) - 1, value)

    def delete_key(self, i):
        self.heap[i], self.heap[-1] = self.heap[-1], self.heap[i]
        self.heap.pop()
        self.heap.max_heapify(self.heap, i)

    def print_queue(self):
        print(self.heap)


def main():
    # my_arr = [500, 23, 56, 57, 478, 479, 900]
    my_arr = [16, 14, 10, 8, 9, 7, 3, 2, 4, 1]
    my_queue = PriorityQueue(my_arr)
    my_queue.print_queue()
    my_queue.heap_increase_key(8, 16)
    my_queue.print_queue()
    my_queue.max_heap_insert(100)
    my_queue.print_queue()
    my_queue.delete_key(3)
    my_queue.print_queue()

if __name__ == '__main__':
    main()
