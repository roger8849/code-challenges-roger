from typing import List

def count_occurrences_of_element_recursive2(array: List, k: int, n: int,  index = 0) -> int:
    '''
        Count occurrences of element
    '''
    # Base case: element not found.
    if index == n:
        return 0
    # Induction step the element was found add them to the result
    # Induction hipothesis the element should be in the smaller array.
    if array[index] == k:
        return 1 + count_occurrences_of_element_recursive2(array, k, n, index + 1)
    else:
        return count_occurrences_of_element_recursive2(array, k, n, index + 1)
    

def main():
    # Element to find.
    k = 13
    a = [1,2,3,4,5]
    print(f'The element k = {k} exist in the array {a} {count_occurrences_of_element_recursive2(a, k, len(a))} times')
    b = [1,2,13,3,4,5]
    print(f'The element k = {k} exist in the array {b} {count_occurrences_of_element_recursive2(b, k, len(b))} times')
    c = [13,2,13,3,4,13]
    print(f'The element k = {k} exist in the array {c} {count_occurrences_of_element_recursive2(c, k, len(c))} times')

if __name__ == "__main__":
    main()