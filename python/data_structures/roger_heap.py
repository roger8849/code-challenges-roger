from inspect import _void


class RogerHeap:
    def __init__(self, heap=list(), is_min_heap=True):
        self.heap = heap
        self.is_min_heap = is_min_heap

    def insert(self, value: int) -> _void:
        """Insert a value in the heap

        Args:
            value (int): The value that will be inserted inside the heap.

        Returns:
            _void: does not return anything.
        """        
        self.heap.append(value)
        self.up_heapify()
    
    def peek(self) -> int:
        return self.heap[0]

    def pop(self) -> int:
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        val = self.heap.pop()
        self.down_heapify()
        return val
    
    def get_children_index(self, parentIndex=0) -> list:
        return (parentIndex*2)+1, (parentIndex*2)+2
    
    def get_parent_index(self, childIndex=0) -> int:
        return (childIndex - 1)//2 if childIndex > 0 else 0
    
    def up_heapify(self) -> _void:
        if self.heap:
            current_index = len(self.heap) - 1
            parent_index = self.get_parent_index(current_index)
            while current_index > 0 and self.compare_values(self.heap[current_index], self.heap[parent_index]):
                self.heap[current_index], self.heap[parent_index] = self.heap[parent_index], self.heap[current_index]
                current_index = parent_index
                parent_index = self.get_parent_index(current_index)
    
    def down_heapify(self) -> _void:
        if self.heap:
            current_index = 0
            n = len(self.heap)
            while True:
                left_index, right_index = self.get_children_index(current_index)
                min_index = current_index
                if left_index < n and self.compare_values(self.heap[left_index],self.heap[min_index]):
                    min_index = left_index
                
                if right_index < n and self.compare_values(self.heap[right_index],self.heap[min_index]):
                    min_index = right_index

                if min_index == current_index:
                    break
                else:
                    self.heap[current_index], self.heap[min_index] = self.heap[min_index], self.heap[current_index]
                    current_index = min_index
                

    def compare_values(self, val1: int, val2: int)-> bool:
        if self.is_min_heap:
            return val1 < val2
        else:
            return val1 > val2
        
    def flush(self):
        self.heap = list()
        

minHeap = RogerHeap()

minHeap.insert(5)
print(minHeap.heap)
minHeap.insert(2)
print(minHeap.heap)
minHeap.insert(7)
print(minHeap.heap)
minHeap.insert(1)
print(minHeap.heap)

minHeap.pop()
print(minHeap.heap)

minHeap.insert(-1)
print(minHeap.heap)

print('##################')


max_heap = RogerHeap(heap=[], is_min_heap= False)
# max_heap.is_min_heap= False
# max_heap.flush()

max_heap.insert(5)
print(max_heap.heap)
max_heap.insert(2)
print(max_heap.heap)
max_heap.insert(40)
print(max_heap.heap)
max_heap.insert(9000)
print(max_heap.heap)
max_heap.insert(150)
print(max_heap.heap)
max_heap.insert(7)
print(max_heap.heap)
max_heap.insert(1)
print(max_heap.heap)
max_heap.pop()
print(max_heap.heap)
max_heap.insert(-1)
print(max_heap.heap)