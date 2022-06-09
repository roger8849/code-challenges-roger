'''
    Check if an array is sorted using recursion
'''

def is_palindrome(a, n, start, end) -> bool:
    # Base case
    if start >= end:
        return True
    # Induction hiphotesis sub problem is also palindrome
    small_answer = is_palindrome(a, n, start + 1, end - 1)
    # Induction step
    return small_answer and a[start] == a[end]


def main():
    a = [1,2,3,2,1]
    n = len(a)
    print(f'Array a = {a} is palindrome {is_palindrome(a, n, 0, n-1)}')
    b = [1,2,6,4,5,6]
    n = len(a)
    print(f'Array b = {b} is palindrome {is_palindrome(b, n, 0, n-1)}')
    c = [2]
    n = len(c)
    print(f'Array c = {c} is palindrome {is_palindrome(c, n, 0, n-1)}')

if __name__ == "__main__":
    main()