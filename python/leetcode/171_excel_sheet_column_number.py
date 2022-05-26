'''
171. Excel Sheet Column Number
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
'''

def titleToNumber(columnTitle: str) -> int:
    ASCII_CHARS_BEFORE_A = 64
    ENG_NUM_CHARS = 26

    answer = int()

    # if empty answer is 0
    if len(columnTitle)==0: return answer

    pow = 1
    
    # Iterating backwards
    for i in range(len(columnTitle)-1, 0-1, -1):
        letter = columnTitle[i].upper()
        # Get asccii substract chars before A to make A=1
        # then multiply pow due the column number
        answer += (ord(letter) - ASCII_CHARS_BEFORE_A) * pow
        # Then augment pow in 26 chars to determine next iteration
        pow *=ENG_NUM_CHARS

    return answer
    

def main():
    print(titleToNumber('A'))
    print(titleToNumber('AB'))
    print(titleToNumber('ZY'))
    

if __name__ == "__main__":
    main()