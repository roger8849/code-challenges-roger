'''
    This function calculates the sum of the array using recursion
'''
def array_sum(*array):
    '''
    Cutting the array in using the last element
    '''
    # Base case
    if len(array) == 0:
        return 0
    # Induction hipotesis
    small_answer = array_sum(*array[0:len(array)-1])

    #Induction step
    return array[len(array) - 1] + small_answer

def array_sum2(*array):
    '''
    Cutting the array the array in using the first element
    '''
    # Base case
    if len(array) == 0:
        return 0
    # Induction hipotesis
    small_answer = array_sum(*array[1])

    #Induction step
    return array[0] + small_answer

def main():
    a = [1,2,3,4]
    print(f'Sum of elements of a = {a} is {array_sum(*a)}')
    b = [2,2]
    print(f'Sum of elements of b = {b} is {array_sum(*b)}')
    c = [1,10,100,1000]
    print(f'Sum of elements of c = {c} is {array_sum(*c)}')

if __name__ == "__main__":
    main()