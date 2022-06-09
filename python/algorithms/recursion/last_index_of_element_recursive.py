def last_index_of_recursive(array, k, index) -> int:
    '''
        Find first index of element. -1 if not found.
    '''
    # Base case: element not found.
    if index < 0:
        return -1
    # Induction step the element was found
    if array[index] == k:
        return index
    # Induction hipothesis the element should be in the smaller array.
    small_answer = last_index_of_recursive(array, k, index - 1)
    return small_answer

def main():
    # Element to find.
    k = 13
    a = [1,2,3,4,5]
    print(f'The element k = {k} exist in the array {a} in the last index {last_index_of_recursive(a, k, len(a) - 1)}')
    b = [1,2,13,3,4,5]
    print(f'The element k = {k} exist in the array {b} in the last index {last_index_of_recursive(b, k, len(b) - 1)}')
    c = [13,2,13,3,4,13]
    print(f'The element k = {k} exist in the array {c} in the last index {last_index_of_recursive(c, k, len(c) - 1)}')

if __name__ == "__main__":
    main()