'''
168. Excel Sheet Column Title
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

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

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 231 - 1
'''

def convertToTitle(columnNumber: int) -> str:
    ASCII_CHARS_BEFORE_A = 64
    ENG_NUM_CHARS = 26

    answer = str()

    while columnNumber > 0:
        mod = columnNumber % ENG_NUM_CHARS
        # Corner case when the value is Z the mod will be 0
        if(mod==0):
            mod=ENG_NUM_CHARS
        # Need to add the Chars before A so chr function will get A
        answer = chr(mod+ASCII_CHARS_BEFORE_A) + answer
        
        # Corner case when the value is Z the mod will be 0
        if columnNumber % ENG_NUM_CHARS == 0:
            columnNumber //= ENG_NUM_CHARS
            columnNumber -=1
        else:
            columnNumber //= ENG_NUM_CHARS
    return answer
    

def main():
    print(convertToTitle(1))
    print(convertToTitle(28))
    print(convertToTitle(701))
    

if __name__ == "__main__":
    main()
