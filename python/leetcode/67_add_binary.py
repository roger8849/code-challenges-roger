

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = str()
        carry = 0
        a, b, a_size, b_size = a[::-1], b[::-1], len(a), len(b)
        for i in range(max(a_size, b_size)):
            digitA = ord(a[i]) - ord('0') if i < a_size else 0
            digitB = ord(b[i]) - ord('0') if i < b_size else 0

            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2

        if carry:
            res = '1' + res
        return res

        
def main():
    solution = Solution()
    a , b = "11", "1"
    print(f'Add binary of {a} and {b} is {solution.addBinary(a,b)}')
    a , b = "1010", "1011"
    print(f'Add binary of {a} and {b} is {solution.addBinary(a,b)}')
    

if __name__ == "__main__":
    main()