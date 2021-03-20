package co.edu.roger.leetcode;

import java.util.AbstractMap;
import java.util.Stack;

/*
 * Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them
 * causing the left and the right side of the deleted substring to concatenate together.
 *
 * We repeatedly make k duplicate removals on s until we no longer can.
 *
 * Return the final string after all such duplicate removals have been made.
 *
 * It is guaranteed that the answer is unique.
 *
 *
 *
 * Example 1:
 *
 * Input: s = "abcd", k = 2
 * Output: "abcd"
 * Explanation: There's nothing to delete.
 * Example 2:
 *
 * Input: s = "deeedbbcccbdaa", k = 3
 * Output: "aa"
 * Explanation:
 * First delete "eee" and "ccc", get "ddbbbdaa"
 * Then delete "bbb", get "dddaa"
 * Finally delete "ddd", get "aa"
 * Example 3:
 *
 * Input: s = "pbbcggttciiippooaais", k = 2
 * Output: "ps"
 *
 *
 * Constraints:
 *
 * 1 <= s.length <= 10^5
 * 2 <= k <= 10^4
 * s only contains lower case English letters.
 */
public class Solution1209RemoveAllAdjacentDuplicatesInString {
    // Solution with K= 2
//    public String removeDuplicates(String S) {
//        Stack<Character> characters = new Stack<>();
//        StringBuilder solution = new StringBuilder();
//        for (int i = 0; i < S.length(); i++) {
//            // Stack is empty then push
//            if (characters.empty()) {
//                characters.push(S.charAt(i));
//            // If different then not adjacent.
//            } else if (!characters.peek().equals(S.charAt(i))) {
//                characters.push(S.charAt(i));
//            // Char at top is equals to index then remove it.
//            } else {
//                characters.pop();
//            }
//        }
//        while (!characters.empty()) {
//            solution.insert(0, characters.pop());
//        }
//        return solution.toString();
//    }

    public String removeDuplicates(String S, int k) {
        Stack<AbstractMap.SimpleEntry<Character, Integer>> characters = new Stack<>();
        StringBuilder solution = new StringBuilder();
        AbstractMap.SimpleEntry<Character, Integer> pair;
        for (int i = 0; i < S.length(); i++) {
            int count = 0;
            // Stack is empty then push || If different then not adjacent.
            if (characters.empty() || !characters.peek().getKey().equals(S.charAt(i))) {
                // found one character.
                count++;
                pair = new AbstractMap.SimpleEntry<>(S.charAt(i), count);
                characters.push(pair);
            // Char at top is equals to index then remove it.
            } else {

                // Increasing the count of chars
                pair = characters.pop();
                count = pair.getValue() + 1;
                // If chars meet conditions to be removed then pop.
                if(count < k) {
                    pair.setValue(count);
                    characters.push(pair);
                } else {
                }
            }
        }
        while (!characters.empty()) {
            pair = characters.pop();
            Character character = pair.getKey();
            for (int i = 1; i <= pair.getValue(); i++) {
                solution.insert(0, character);
            }
        }
        return solution.toString();
    }

    public static void main(String[] args) {
        Solution1209RemoveAllAdjacentDuplicatesInString solution = new Solution1209RemoveAllAdjacentDuplicatesInString();
        String example1 = "deeedbbcccbdaa";
        System.out.println(solution.removeDuplicates(example1, 3));
    }

}
