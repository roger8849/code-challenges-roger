package co.edu.roger.glovo;

import java.util.Collection;
import java.util.HashMap;

public class SolutionProblem2 {
    public boolean areAnagram(String word1, String word2) {

        if (word1 == null && word2 == null) {
            return false;
        }
        if (word1.length() != word2.length()) {
            return false;
        }
        HashMap<Character, Integer> dictionary = new HashMap<>();
        for (int i = 0; i < word1.length(); i++) {
            char char1 = word1.charAt(i);
            char char2 = word2.charAt(i);

            if (dictionary.containsKey(char1)) {
                Integer value = dictionary.get(char1);
                dictionary.put(char1, ++value);
            } else {
                dictionary.put(char1, 1);
            }

            if (dictionary.containsKey(char2)) {
                Integer value = dictionary.get(char2);
                dictionary.put(char2, --value);
            } else {
                dictionary.put(char2, -1);
            }
        }

        Collection<Integer> values = dictionary.values();
        /*  */
        boolean result = values.stream().anyMatch( v -> v != 0);
        return !result;
    }

    // S(h) h-> size of alphabet - O(n + h) n-> size of string
    public static void main(String[] args) {

        SolutionProblem2 solution = new SolutionProblem2();
        String example11 = "ABCD";
        String example12 = "DABC";
        System.out.println("are anagrams? " + solution.areAnagram(example11, example12));

        String example21 = "AABB";
        String example22 = "BBAA";
        System.out.println("are anagrams? " + solution.areAnagram(example21, example22));

        String example31 = "AAAB";
        String example32 = "AAB";
        System.out.println("are anagrams? " + solution.areAnagram(example31, example32));

        String example41 = "AAAB";
        String example42 = "AABC";
        System.out.println("are anagrams? " + solution.areAnagram(example41, example42));
    }

}
