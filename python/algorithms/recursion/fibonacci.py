'''
Implements the Fibonacci series using recursion
'''
from timeit import default_timer as timer

# To avoid exponential complexity then memorize the values already calculated to reduce the time
def fibonacciMemorization(n: int, mem) -> int :
    # If memory contains value return it
    if n in mem:
        return mem[n]
    # Induction step 1 and 2
    small_answer2 = fibonacciMemorization(n-2, mem)
    small_answer1 = fibonacciMemorization(n-1, mem)
    # Induction steps.
    answer = small_answer1 + small_answer2
    mem[n] = answer
    return answer

# Classic fibonacci algorithm recursive.
def fibonacci(n: int) -> int:
    #  base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Induction hipothesis 1 and 2
    small_answer = fibonacci(n-1) + fibonacci(n-2) # Assume smaller is true
    #  Induction step.
    return small_answer 

def main():
    n = int(input("Enter a positive number:"))
    print('--- Normal method ---')
    start=timer()
    print(f'nˆth fibonnacci number is {fibonacci(n)}')
    end=timer()
    print(f'Time in seconds {(end-start):.10f}')

    print('--- Memorization method ---')
    start=timer()
    # Base case
    mem = {0:0, 1:1}
    print(f'nˆth fibonnacci number is {fibonacciMemorization(n, mem)}')
    end=timer()
    print(f'Time in seconds {(end-start):.10f}')


if __name__ == "__main__":
    main()