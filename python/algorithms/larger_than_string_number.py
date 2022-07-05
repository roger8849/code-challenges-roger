
def largerThanHelper(number1: str, number2: str)-> bool:
    '''
        Compare one by one the numbers
    '''
    if len(number1) > len(number2):
        return True
    elif len(number1) < len(number2):
        return False
    else:
        for i in range(len(number1)):
            if number1[i] > number2[i]:
                return True
            elif number1[i] < number2[i]:
                return False
    # numbers are equal
    return False

def largerThan(number1: str, number2: str)-> bool:
    '''
        Rules:
        cannot convert string to int.
        if not number1 then false if not number2 then true
        compare negatives
    '''
    # handling nulls
    if not number1:
        return False
    elif not number2:
        return True
    # if negatives
    if number1[0] == '-' and number2[0] != '-':
        return False
    elif number1[0] != '-' and number2[0] == '-':
        return True
    else:
        # if both negatives slice and invert numbers
        if number1[0] == '-' and number2[0] == '-':
            return largerThanHelper(number2[::1], number1[::1])
        #if both positives compare normal
        return largerThanHelper(number1, number2)


def main():
    assert largerThan('-500', '-1000')
    assert not largerThan('-500', '-50')
    assert largerThan('500', '-50')
    assert not largerThan('-500', '50')
    assert largerThan('1','0')
    assert not largerThan('0', '1')

if __name__ == "__main__":
    main()