package co.edu.roger.geeksforgeeks;

import java.util.HashSet;
import java.util.Set;

/*Consonants and Vowels check - Java
    EasyAccuracy: 46.8%Submissions: 17362Points: 2
    You are given a string s containing only lowecase letters. You need to count the number of vowels and the number of consonants.

    If vowel count > consonant count then print - “Yes”(without quotes).
    If vowel count < consonant count then print - “No”(without quotes).
    If vowel count = consonant count then print - “Same”(without quotes).
    Example 1:

    Input:
    the quick brown fox jumps over the lazy dog

    Output:
    No
    Example 2:

    Input:
    aaaaaa

    Output:
    Yes
    Your Task:
    Since this is a function problem, you don't need to take any input. Just complete the function checkString(string  s) that take s as input and produces output.

    Constraints:
    1 <= |s| <= 100
*/

public class ConsontantsVowelsCheck {
    static void checkString(String s) {
        int v = 0;
        int c = 0;

        // Your code here
        Set<Integer> vowelsArr = new HashSet<>();
        vowelsArr.add('a' - 'a');
        vowelsArr.add('e' - 'a');
        vowelsArr.add('i' - 'a');
        vowelsArr.add('o' - 'a');
        vowelsArr.add('u' - 'a');
        
        for (int i = 0; i < s.length(); i++) {
            int charIdx = s.charAt(i) - 'a';
            if (vowelsArr.contains(charIdx)) {
                v++;
            } else {
                // If char is not a vowel but is a letter.
                if (charIdx > 0 && charIdx <= 26) {
                    c++;
                }
            }
        }

        if (v > c)
            System.out.print("Yes");
        else if (c > v)
            System.out.print("No");
        else
            System.out.print("Same");

        System.out.println();
    }
    public static void main(String[] args) {
        ConsontantsVowelsCheck solution = new ConsontantsVowelsCheck();
        solution.checkString("ai u e o");
    }
}
