package co.edu.roger.leetcode;

import java.util.Stack;

/*
 *Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
 *
 *We repeatedly make duplicate removals on S until we no longer can.
 *
 *Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
 *
 *
 *
 *Example 1:
 *
 *Input: "abbaca"
 *Output: "ca"
 *Explanation:
 *For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
 *
 *
 *Note:
 *
 *1 <= S.length <= 20000
 *S consists only of English lowercase letters.
 */
public class Solution1047RemoveAllAdjacentDuplicatesInString {
    public String removeDuplicates(String S) {
        Stack<Character> characters = new Stack<>();
        StringBuilder solution = new StringBuilder();
        for (int i = 0; i < S.length(); i++) {
            // Stack is empty then push
            if (characters.empty()) {
                characters.push(S.charAt(i));
            // If different then not adjacent.
            } else if (!characters.peek().equals(S.charAt(i))) {
                characters.push(S.charAt(i));
            // Char at top is equals to index then remove it.
            } else {
                characters.pop();
            }
        }
        while (!characters.empty()) {
            solution.insert(0, characters.pop());
        }
        return solution.toString();
    }

    public static void main(String[] args) {
        Solution1047RemoveAllAdjacentDuplicatesInString solution = new Solution1047RemoveAllAdjacentDuplicatesInString();
        String example1 = "abbaca";
        System.out.println(solution.removeDuplicates(example1));
    }

}
