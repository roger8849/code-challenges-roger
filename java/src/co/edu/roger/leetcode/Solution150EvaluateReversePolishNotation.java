package co.edu.roger.leetcode;

import java.util.Arrays;
import java.util.Stack;

/*
 * Evaluate the value of an arithmetic expression in Reverse Polish Notation.
 *
 * Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
 *
 * Note that division between two integers should truncate toward zero.
 *
 * It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a
 * result, and there will not be any division by zero operation.
 *
 *
 * */
public class Solution150EvaluateReversePolishNotation {

    /**
     * Using stack approach to evaluate reverse polish notation.
     *
     * @param tokens
     * @return
     */
    public int evalRPN(String[] tokens) {
        Stack<Integer> evaluatedValue = new Stack<>();
        for (String token : tokens) {
            int result = 0;
            if (Arrays.asList("+", "-", "*", "/").stream().anyMatch(operator -> operator.equals(token))) {
                result = operateTerms(evaluatedValue, token, result);
                evaluatedValue.push(result);
            } else {
                int operand = Integer.parseInt(token);
                evaluatedValue.push(operand);
            }
        }
        return evaluatedValue.pop();
    }

    private int operateTerms(Stack<Integer> evaluatedValue, String token, int result) {
        int operand1 = evaluatedValue.pop();
        int operand2 = evaluatedValue.pop();
        switch (token) {
            case "+":
                result = operand2 + operand1;
                break;
            case "-":
                result = operand2 - operand1;
                break;
            case "*":
                result = operand2 * operand1;
                break;
            case "/":
                result = operand2 / operand1;
                break;
        }
        return result;
    }

    public static void main(String[] args) {
        Solution150EvaluateReversePolishNotation solution = new Solution150EvaluateReversePolishNotation();

        String example1[] = {"2", "1", "+", "3", "*"};
        System.out.println("Example: " + Arrays.toString(example1));
        System.out.println("Result: " + solution.evalRPN(example1));

        String example2[] = {"4", "13", "5", "/", "+"};
        System.out.println("Example: " + Arrays.toString(example2));
        System.out.println("Result: " + solution.evalRPN(example2));
    }

}
