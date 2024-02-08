'''
    This class implements a function that calculates the minimum steps to reach 1.
    
    Using the following rules:
    
    * Divide by 3
    * Divide by 2
    * Substract 1
    
    3 steps:
        10 -1 -> 9 / 3 -> 2-1 -> 1
    
'''

import sys
from timeit import default_timer as timer

def minimumStepsToOneRecursive(n: int) -> int:
    """Implements the minimum steps to one in a recursive way.
    
    NOT EFFICIENT because is recalculating values

    Args:
        n (int): starting point to reach 1

    Returns:
        int: minimum numbers to reach 1.
    """        
    # Base Case
    if n == 1: return 0
    
    x =  minimumStepsToOneRecursive(n-1)
    y = z = sys.maxsize
    
    if n % 2 == 0:
        y = minimumStepsToOneRecursive(n//2)
    
    if n % 3 == 0:
        z = minimumStepsToOneRecursive(n//3)
    
    small_answer = 1 + min(x,y,z)
    
    return small_answer

def minimumStepsToOneMemorization(n: int, mem={1:0}) -> int:
    """Implements the minimum steps to one in a recursive way using memory

    Args:
        n (int): starting point to reach 1

    Returns:
        int: minimum numbers to reach 1.
    """        
    # Base Case
    if n in mem: 
        return mem[n]
    
    x =  minimumStepsToOneMemorization(n-1, mem)
    y = z = sys.maxsize
    
    if n % 2 == 0:
        y = minimumStepsToOneMemorization(n//2, mem)
    
    if n % 3 == 0:
        z = minimumStepsToOneMemorization(n//3, mem)
    
    small_answer = 1 + min(x,y,z)
    mem[n] = small_answer
    return small_answer

def minimumStepsToOneDynamicProgramming(n: int) -> int:
    """Implements the minimum steps to one in a recursive way using iterative method

    Args:
        n (int): starting point to reach 1

    Returns:
        int: minimum numbers to reach 1.
    """        
    # Base Case
    if n  <= 1:
        return 0
    if n == 2:
        return 1
    if n == 3: 
        return 1
    
    a =  [-1] * (n+1)
    a[0], a[1], a[2], a[3] = 0, 0, 1, 1

    for i in range(4, n+1):
        x = a[i-1]
        y = z = sys.maxsize
        if i % 2 == 0:
            y = a[i//2]
        if i % 3 == 0:
            y = a[i//3]
            
        a [i] = 1 + min(x,y,z)
    return a[-1]
    
    
    
    

n = int(input("Enter a positive number:"))
print('--- Normal Recursion method ---')
start=timer()
print(f'nˆth fibonnacci number is {minimumStepsToOneRecursive(n)}')
end=timer()
print(f'Time in seconds {(end-start):.10f}')

print('--- Memorization method ---')
start=timer()
print(f'nˆth fibonnacci number is {minimumStepsToOneMemorization(n)}')
end=timer()
print(f'Time in seconds {(end-start):.10f}')

print('--- Dynamic programming method ---')
start=timer()
print(f'nˆth fibonnacci number is {minimumStepsToOneDynamicProgramming(n)}')
end=timer()
print(f'Time in seconds {(end-start):.10f}')
