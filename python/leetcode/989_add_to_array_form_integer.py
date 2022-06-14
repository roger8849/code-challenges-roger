



class Solution(object):
    def addToArrayForm(self, num, k):
        strs=''
        for i in num:
            strs+=str(i)
            x=int(strs)+k
            l=list(map(int,str(x)))
        return l

def main():
    solution = Solution()
    digits, k = [1,2,0,0], 34
    print(f'{digits} + {k} = {solution.addToArrayForm(digits, k)}')
    digits, k = [2,7,4], 181
    print(f'{digits} + {k} = {solution.addToArrayForm(digits, k)}')
    digits, k = [2,1,5], 806
    print(f'{digits} + {k} = {solution.addToArrayForm(digits, k)}')

if __name__ == "__main__":
    main()