package co.edu.roger.leetcode;

/*
* Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
*
* For example:
*
* A -> 1
* B -> 2
* C -> 3
* ...
* Z -> 26
* AA -> 27
* AB -> 28
*/
public class Solution171ExcelSheetColumnNumber {
    public int titleToNumber(String columnTitle) {
        int answer = 0;
        // Multiplier some times gets really big
        long multiplier = 1;

        for (int i = columnTitle.length() - 1; i >= 0 ; i--) {
            answer = answer + (int)((columnTitle.charAt(i) - 64)* multiplier);
            // If more chars, then we need to multiply by 26.
            multiplier = multiplier * 26;
        }
        return answer;
    }

    public static void main(String[] args) {
        Solution171ExcelSheetColumnNumber solution = new Solution171ExcelSheetColumnNumber();
        String example1 = "A";
        System.out.println(solution.titleToNumber(example1));
        String example2 = "AAA";
        System.out.println(solution.titleToNumber(example2));
    }
}
