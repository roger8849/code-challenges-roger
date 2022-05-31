'''
This script implements factorial problem using recursion.
'''

def factorial(n: int) -> int:
    # Base case
    if n == 0: 
        return 1
    # Induction hipothesis smaller problem is true
    smallAnswer = n * factorial(n-1)
    # Induction step.
    return smallAnswer

def main():
    print(f'Factorial = {factorial(int(input("Insert a number: ")))}')

if __name__ == "__main__":
    main()