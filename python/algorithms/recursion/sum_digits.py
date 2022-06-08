'''
Sum digits using recursion

'''

def sum_digits(n: int) -> int:
    # Base case
    if n == 0 :
        return 0
    small_answer = sum_digits(n//10)
    last_digit = n % 10
    return small_answer + last_digit
    
def main():
    print(sum_digits(int(input('Insert a number: '))))

if __name__ == "__main__":
    main()