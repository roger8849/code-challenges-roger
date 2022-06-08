'''
    This script implement the multiplication using recursion by adding the numbers
'''
def recursion_multiplication(n: int, m: int)-> int:
    # Base case
    if n == 0:
        return 0

    # Induction hipothesis smaller problem is true
    small_answer = m + recursion_multiplication(n-1, m)
    # Induction step
    return small_answer

def main():
    m = int(input('Enter m: '))
    n = int(input('Enter n: '))

    print(f'Result is {recursion_multiplication(n,m)}')



if __name__ == "__main__":
    main()