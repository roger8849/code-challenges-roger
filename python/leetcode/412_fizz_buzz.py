'''
412. Fizz Buzz
Easy

Share
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104
'''


from typing import List

fizz_str = 'Fizz'
buzz_str = 'Buzz'
fizz_buzz_lst = list()

# This approach can be extended by adding more elements in the Map
# However is less performant because we're using extra space
def fizzBuzzMap(n: int) -> List[str]:
    fizz_buzz_dict = {
            3:fizz_str, 
            5:buzz_str
        }
    # fb_keys = fizz_buzz_dict.keys()
    
    # Starts from 1 -> n inclusive
    for i in range(1, n+1):
        replacement = ''
        # Check for keys and values 
        for key, value in fizz_buzz_dict.items():
            if i % key == 0:
                replacement+=value
        # If i is not divisible by any key then add i
        if replacement == '':
            replacement = str(i)
        fizz_buzz_lst.append(replacement)
    return fizz_buzz_lst

def fizzBuzzNaiveNoExtraSpace(n: int) -> List[str]:
    # Starts from 1 -> n inclusive
    for i in range(1, n+1):
        is_fizz = i % 3 == 0
        is_buzz = i % 5 == 0
        if is_fizz and is_buzz :
            fizz_buzz_lst.append(fizz_str+buzz_str)
        elif is_fizz:
            fizz_buzz_lst.append(fizz_str)
        elif is_buzz:
            fizz_buzz_lst.append(buzz_str)
        else:
            fizz_buzz_lst.append(str(i))
    return fizz_buzz_lst

def fizzBuzzNaive(n: int) -> List[str]:
    # Starts from 1 -> n inclusive
    for i in range(1, n+1):
        is_fizz = i % 3 == 0
        is_buzz = i % 5 == 0
        if is_fizz and is_buzz :
            fizz_buzz_lst.append(fizz_str+buzz_str)
        elif is_fizz:
            fizz_buzz_lst.append(fizz_str)
        elif is_buzz:
            fizz_buzz_lst.append(buzz_str)
        else:
            fizz_buzz_lst.append(str(i))
    return fizz_buzz_lst


def main():
    n = input('Enter a number to print fizz buzz')
    print(f'Naive approach {fizzBuzzNaive(int(n))}')
    fizz_buzz_lst.clear()
    print(f'Map approach {fizzBuzzMap(int(n))}')

if __name__ == "__main__":
    main()