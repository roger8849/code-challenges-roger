'''
    Check if an array is sorted using recursion
'''

def array_is_sorted(a, start=0) -> bool:
    # Base case
    if len(a) <= 1 :
        return True
    # Induction hiphotesis sub problem is also sorted
    small_answer = array_is_sorted(a[start + 1:])
    # Induction step
    return small_answer and a[start] <= a[start + 1]


def main():
    a = [1,2,3,4,5,6]
    print(f'Array a = {a} is sorted {array_is_sorted(a)}')
    b = [1,2,6,4,5,6]
    print(f'Array b = {b} is sorted {array_is_sorted(b)}')

if __name__ == "__main__":
    main()