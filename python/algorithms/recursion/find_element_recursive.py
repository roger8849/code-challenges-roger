def find_element_recursive(k, n, *array) -> bool:
    # Base case: element not found.
    if n == 0:
        return False
    # Induction step the element was found
    if array[0] == k:
        return True
    # Induction hipothesis the element should be in the smaller array.
    small_answer = find_element_recursive( k, n-1, *array[1:])
    return small_answer

def main():
    # Element to find.
    k = 13
    a = [1,2,3,4,5]
    
    print(f'The element k = {k} exist in the array {a} is {find_element_recursive(k, len(a), *a)}')
    b = [1,2,13,3,4,5]
    print(f'The element k = {k} exist in the array {b} is {find_element_recursive(k, len(b), *b)}')
    c = [13,2,13,3,4,13]
    print(f'The element k = {k} exist in the array {c} is {find_element_recursive(k, len(c), *c)}')

if __name__ == "__main__":
    main()