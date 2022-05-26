'''150. Evaluate Reverse Polish Notation
Medium

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].'''
from typing import List
from queue import LifoQueue
import math
# ["4","13","5","/","+"]
def evalRPN(tokens: List[str]) -> int:
    # result = int
    operands = ['+', '-', '*','/']
    result_stack = LifoQueue()
    
    for token in tokens :
        if token in operands :
            operation = int()
            int_1 = result_stack.get()
            int_2 = result_stack.get()
            if token == '+':
                operation = int_2 + (int_1)
            elif token == '-':
                operation = int_2 - (int_1)
            elif token == '*':
                operation = int_2 * (int_1)
            elif token == '/':
                operation = int_2 / (int_1)
                operation = math.trunc(operation)
            result_stack.put(operation)
        else:
            result_stack.put(int(token))

    return result_stack.get()

def main():
    # print(evalRPN(["2","1","+","3","*"]))
    # print(evalRPN(["4","13","5","/","+"]))
    print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

if __name__ == "__main__":
    main()