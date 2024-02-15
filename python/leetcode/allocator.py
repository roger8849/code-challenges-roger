# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math


class Allocator:
    def __init__(self, N: int):
        # Implement your solution here
        if N < 8 or N > 1024:
            raise ValueError("N must be between 8 and 1024")

     
        if not math.log2(N).is_integer():
            raise ValueError("N Must be a power of 2")

        self.N = N
        self.allowed_sizes = (1,4,8)
        # self.occuppied_pos =  dict()
        # self.free_pos = set(range(N))

        # print(self.occuppied_pos)
        # print(self.free_pos)
        self.memory = [-1] * N
        # print(self.memory)

    def alloc(self, size: int) -> int:
        # Implement your solution here
        if size not in self.allowed_sizes:
            raise ValueError("Size must be 1, 4 or 8")
        # iterate if can store the variable
        memory_start = -1
        # not going out of range of the memory.
        for i in range(self.N):
            # free memory available
            if self.memory[i] == -1:
                # start iterating on the free position
                if memory_start == -1:
                    memory_start = i
                # print(memory_start)
                if (i - memory_start + 1) == size: # Found enough free space.
                    for j in range(memory_start, i+1):
                        self.memory[j] = memory_start # Add the base index to the memory position
                    return memory_start # position used.
            else: # Memory position is filled.
                memory_start = -1
        # print(self.memory)
        # couldn't allocate the memory
        return -1

    def free(self, address: int) -> None:
        # Implement your solution here
        if address < 0 or address >= self.N:
            raise ValueError("Address position not valid")

        # Address is always valid then i shouldn't check for boundaries.
        idx_to_be_freed = self.memory[address]

        for i in range(self.N):
            if self.memory[i] == idx_to_be_freed:
                self.memory[i] = -1 # Freeing the memory
        
        # print(self.memory)
        


#a = Allocator(16)
#assert a.alloc(4) == 0 
#assert a.alloc(8) == 8 # bytes 8-15 are allocated
#assert a.alloc(4) == 4 # bytes 4-7 are allocated
#a.free(0)
#print(a.memory)
#assert a.alloc(1) == 0
#assert a.alloc(1) == 1   # byte 1 is allocated
#a.free(4) #        |    -   | bytes 4-7 are freed
#print(a.memory)
#a.free(1) #        |    -   | byte 1 is freed
#print(a.memory)
#a.free(0)  #       |    -   | byte 0 is freed
#assert a.alloc(8)  == 0  # | bytes 0-7 are allocated|        |   to a variable of size 8



b = Allocator(8) #    | create an allocator for
#assert b                ==       |   8 bytes of memory
assert b.alloc(8) == 0 #    | bytes 0-7 are allocated
#assert b                ==   #    |   to a variable of size 8
assert b.alloc(1) == -1 #    | there are no free bytes
b.free(0)
assert b.alloc(1)       == 0 #    | byte 0 is allocated
assert b.alloc(4)       == 1 #    | bytes 1-4 are allocated
b.free(0) #       == - #    | byte 0 is freed
assert b.alloc(4)       == -1 #    | there are no 4 consecutive
#assert b                ==   #    |   free bytes