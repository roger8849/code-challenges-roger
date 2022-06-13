'''
    Given N the idea is to know how many ways do we have to reach from ground to N if you can do:
    1,2,3 steps at a time for instance for a given N = 3 you can do:
    3 -> 1,1,1
         1,2
         2,1
         3
'''
from timeit import default_timer as timer
from typing import List

def staircase_problem(n: int)-> int:
    '''
        Less code but innefficient.
    '''
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return 0
    return staircase_problem(n-1) + staircase_problem(n-2) + staircase_problem(n-3)

def staircase_problem_memorization(n: int, memory:List)-> int:
    '''
        Uses extra memory but is way more efficient.
    '''
    # base cases are already in memory.
    if n in memory:
        return memory[n]
   
    small_answer1 = staircase_problem_memorization(n-1, memory) 
    small_answer2 = staircase_problem_memorization(n-2, memory) 
    small_answer3 = staircase_problem_memorization(n-3, memory)
    answer = small_answer1 + small_answer2 + small_answer3
    memory[n] = answer
    return answer

def main():
    n = int(input('Enter a number: '))
    print('--- Normal method ---')
    start=timer()
    print(f'Number of ways to go from ground to N = {staircase_problem(n)}')
    end=timer()
    print(f'Time in seconds {(end-start):.10f}')

    print('--- Memorization method ---')
    start=timer()
    memory = {0:1, 1:1, 2:2}
    print(f'Number of ways to go from ground to N = {staircase_problem_memorization(n, memory)}')
    end=timer()
    print(f'Time in seconds {(end-start):.10f}')

if __name__ == "__main__":
    main()