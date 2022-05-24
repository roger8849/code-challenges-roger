package co.edu.roger.leetcode;

/*
 * Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
 *
 * Example 1:
 *
 * Input: s = "A man, a plan, a canal: Panama"
 * Output: true
 * Explanation: "amanaplanacanalpanama" is a palindrome.
 * Example 2:
 *
 * Input: s = "race a car"
 * Output: false
 * Explanation: "raceacar" is not a palindrome.
 */
public class Solution125ValidPalindrome {
    public boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length() - 1;
        if (s != null && s.length() <= 1) {
            return true;
        }
        // Using two indexes O(N) no extra space S(1)
        while (start < end) {
            // If char at start is not alphanumeric, move index.
            while (start < end && !Character.isLetterOrDigit(s.charAt(start))) {
                start++;
            }
            // If char at end is not alphanumeric, move index.
            while (start < end && !Character.isLetterOrDigit(s.charAt(end))) {
                end--;
            }
            if (Character.toUpperCase(s.charAt(start)) != Character.toUpperCase(s.charAt(end))) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution125ValidPalindrome solution = new Solution125ValidPalindrome();
//        String example1 = "A man, a plan, a canal: Panama";
//        System.out.println(solution.isPalindrome(example1));
//        String example2 = "race a car";
//        System.out.println(solution.isPalindrome(example2));
        String example3 = ".,";
        System.out.println(solution.isPalindrome(example3));
    }
}
