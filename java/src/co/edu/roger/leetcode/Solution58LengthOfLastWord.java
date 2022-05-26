package co.edu.roger.leetcode;

public class Solution58LengthOfLastWord {
    public int lengthOfLastWord(String s) {
        int n = s.length();
        int i = 0;
        int lengthLastWord = 0;
        while (i < n) {
            if (s.charAt(i) != ' ') {
                lengthLastWord++;
                i++;
            } else {
                while (i < n && s.charAt(i) == ' ') {
                    i++;
                }
                if(i == n) {
                    return lengthLastWord;
                } else {
                    lengthLastWord = 0;
                }

            }
        }
        return lengthLastWord;
    }

    public static void main(String[] args) {
        Solution58LengthOfLastWord solution = new Solution58LengthOfLastWord();
        
    }
}
