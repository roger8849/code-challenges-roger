
import sys
from typing import List


def secondLargestNumber(a: List) -> int:
    # Base case
    if len(a) < 2:
        return None
    largest = -(sys.maxsize)
    second_largest = largest
    for number in a:

        if number > largest:
            largest, second_largest = number, largest
        elif number == largest:
            second_largest = number
        elif number < largest  and number > second_largest:
            second_largest = number
    return second_largest


def main():
    a = [2]
    assert secondLargestNumber(a) == None

    a = [4,2]
    assert secondLargestNumber(a) == 2

    a = [2,6,4,3,8,1,9]
    assert secondLargestNumber(a) == 8

    a = [2,2,2,2,2,2,2,2]
    assert secondLargestNumber(a) == 2
    

if __name__ == "__main__":
    main()