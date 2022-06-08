'''
    This algorithm implement the geometric the value of k is:
    1 + 1/2^1 + 1/2^2 + 1/2^3 + ... + 1/2ˆk
'''

def geometric_sum(k: int) -> int:
    if k == 0:
        return 1
    #Induction hipothesis
    small_answer = geometric_sum(k-1)
    # Induction step.
    return small_answer + 1 / pow(2, k)


def main():
    k = int(input('Enter a number to calculate geometric sum: '))
    print(f'Geometric sum of k={k} is {geometric_sum(k):.5f}')
    

if __name__ == "__main__":
    main()