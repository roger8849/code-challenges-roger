'''
Implements print of n number using recursion.
'''
from inspect import _void


def recursive_print(n: int, asc=True) -> _void:
    # base case.
    if n < 0:
        return
    # Print in descending order
    if not(asc):
        print(n)
    # Recursive case
    recursive_print( n-1, asc )

    #Print in ascending order.
    if asc:
        print(n)

def main():
    recursive_print(int(input('Insert a number')))
    recursive_print(int(input('Insert a number')), False)

if __name__ == "__main__":
    main()