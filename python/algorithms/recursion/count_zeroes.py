
def count_zeroes(n: int) -> int:
    # Base case
    if n == 0:
        return 0
    
    # Induction hipothesis
    small_answer = count_zeroes(n//10)

    #Induction step, get the last digit.
    last_digit = n % 10

    # Check if digit is 0
    if last_digit == 0:
        return small_answer + 1
    else :
        return small_answer


def main():
    print(f'Number of zeroes {count_zeroes(int(input("Enter a number: ")))}')


if __name__ == "__main__":
    main()