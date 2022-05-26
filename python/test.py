import os
import random

def main():
    tuple_test = [1,2,3,4,55,6,7]
    tuple_test[4] = 5
    print(tuple_test)
    print(os.getenv('PATH'))

    x=random.randint(1,1000)
    print(f'This is the random number {x}')

if __name__ == "__main__":
    main()