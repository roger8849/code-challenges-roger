package co.edu.roger.leetcode;

/*
 * Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
 *
 * Example 1:
 * Input: "aba"
 * Output: True
 * Example 2:
 * Input: "abca"
 * Output: True
 * Explanation: You could delete the character 'c'.
 * Note:
 * The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
 */
public class Solution680ValidPalindromeII {
    /**
     * Function will check substrings aftter removing characters.
     *
     * @param s
     * @param start
     * @param end
     * @return
     */
    public boolean checkIsPalindrome(String s, int start, int end) {
        while (start < end) {
            // If removing chars not work, definitiley is false
            if (s.charAt(start) != s.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }

    /**
     * co.edu.roger.test.Main function will check entirely if is palíndrome.
     * @param s
     * @return
     */
    public boolean validPalindrome(String s) {
        int start = 0;
        int end = s.length() - 1;
        while (start < end) {
            // If so far is palindrome then move indexes
            if(s.charAt(start) == s.charAt(end)) {
                start++;
                end--;
            } else {
                if (checkIsPalindrome(s, start + 1, end) // If deleting start is palindrome [start+1... end]
                        || checkIsPalindrome(s, start, end-1)) { // Or if deleting end [start... end-1]
                    return true;
                } else {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution680ValidPalindromeII solution = new Solution680ValidPalindromeII();

        String example1 = "aba";
        System.out.println(solution.validPalindrome(example1));
        String example2 = "abca";
        System.out.println(solution.validPalindrome(example2));
        String example3 = "absca";
        System.out.println(solution.validPalindrome(example3));
        String example4 = "zabbbba";
        System.out.println(solution.validPalindrome(example4));
    }
}
