''' 
Implements power of Xˆn using recursion
'''

def power(x: int, n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return x
    small_answer = power(x, n-1)
    answer = x * small_answer
    return answer

def main():
    x = int(input('Enter the base: '))
    n = int(input('Enter the power: '))
    print(f'The value of {x}^{n} is {power(x,n)}')

if __name__ == "__main__":
    main()
