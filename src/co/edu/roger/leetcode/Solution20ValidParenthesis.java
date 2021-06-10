package co.edu.roger.leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
/*
* Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

* An input string is valid if:
*
* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
*
*
* Example 1:
*
* Input: s = "()"
* Output: true
* Example 2:
*
* Input: s = "()[]{}"
* Output: true
* Example 3:
*
* Input: s = "(]"
* Output: false
* Example 4:
*
* Input: s = "([)]"
* Output: false
* Example 5:
*
* Input: s = "{[]}"
* Output: true
*
*
* Constraints:
*
* 1 <= s.length <= 104
* s consists of parentheses only '()[]{}'.
* */
public class Solution20ValidParenthesis {


    /*improved solutions using set
    **/
    public boolean isValid(String s) {
        Stack<Character> parenthesisStack = new Stack<>();
        List<Character> openers = new ArrayList<>(){{
            add('(');
            add('[');
            add('{');
        }};
        List<Character> closers = new ArrayList<>(){{
            add(')');
            add(']');
            add('}');
        }};
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            if (openers.contains(currentChar)) { //opening parenthesis.
                parenthesisStack.push(currentChar);
            } else { //Closing parenthesis validation no required.
                char opener = openers.get(closers.indexOf(currentChar));
                // If top of the stack is the right opener
                if (!parenthesisStack.empty() && opener == parenthesisStack.peek()) {
                    parenthesisStack.pop(); // Parenthesis balanced
                } else  {
                    return false; // Parenthesis NOT balanced
                }
            }
        }
        if (parenthesisStack.empty()) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        Solution20ValidParenthesis solution = new Solution20ValidParenthesis();
        System.out.println(solution.isValid("()[]{}"));
        System.out.println(solution.isValid("(]"));
        System.out.println(solution.isValid("([][][][][]{}{}{}{})"));
        System.out.println(solution.isValid("{[]}"));
    }
}
