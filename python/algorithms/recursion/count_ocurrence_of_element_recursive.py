from typing import List

def count_occurrences_of_element_recursive(array: List, k: int, n: int, indexes: List, index = 0) -> int:
    '''
        Find all index of element. -1 if not found.
    '''
    # Base case: element not found.
    if index == n:
        return
    # Induction step the element was found add them to the result
    if array[index] == k:
        indexes.append(index)
    # Induction hipothesis the element should be in the smaller array.
    count_occurrences_of_element_recursive(array, k, n, indexes, index + 1)
    return len(indexes)

def main():
    # Element to find.
    k = 13
    a = [1,2,3,4,5]
    print(f'The element k = {k} exist in the array {a} {count_occurrences_of_element_recursive(a, k, len(a), list())} times')
    b = [1,2,13,3,4,5]
    print(f'The element k = {k} exist in the array {b} {count_occurrences_of_element_recursive(b, k, len(b),list())} times')
    c = [13,2,13,3,4,13]
    print(f'The element k = {k} exist in the array {c} {count_occurrences_of_element_recursive(c, k, len(c),list())} times')

if __name__ == "__main__":
    main()