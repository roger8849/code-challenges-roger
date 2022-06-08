
'''
Count digits using recursion
'''
def count_digits(n: int) -> int:
    if(n==0):
        return 0
    # recursive case
    small_answer = count_digits(n//10)

    return small_answer + 1

def main():
    print(count_digits(int(input('Insert a number'))))

if __name__ == "__main__":
    main()