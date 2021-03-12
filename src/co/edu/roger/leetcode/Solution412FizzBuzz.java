package co.edu.roger.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/*
* Write a program that outputs the string representation of numbers from 1 to n.
* But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
* For numbers which are multiples of both three and five output “FizzBuzz”.*/
public class Solution412FizzBuzz {
    /*Naive approach*/
//    public List<String> fizzBuzz(int n) {
//        List<String> solution = new LinkedList<>();
//        for (int i = 1; i <= n; i++) {
//            boolean isDivisibleBy3 = i % 3 == 0;
//            boolean isDivisibleBy5 = i % 5 == 0;
//            if(isDivisibleBy3 && isDivisibleBy5) {
//                solution.add("FizzBuzz");
//            } else if(isDivisibleBy3) {
//                solution.add("Fizz");
//            } else if(isDivisibleBy5){
//                solution.add("Buzz");
//            } else {
//                solution.add(String.valueOf(i));
//            }
//        }
//        return solution;
//    }

    /*
    * Best approach can be extended.*/
    public List<String> fizzBuzz(int n) {

        // ans list
        List<String> ans = new ArrayList<String>();

        // Hash map to store all fizzbuzz mappings.
        HashMap<Integer, String> fizzBizzDict =
                new HashMap<Integer, String>() {
                    {
                        put(3, "Fizz");
                        put(5, "Buzz");
                    }
                };

        for (int num = 1; num <= n; num++) {

            String numAnsStr = "";

            for (Integer key : fizzBizzDict.keySet()) {

                // If the num is divisible by key,
                // then add the corresponding string mapping to current numAnsStr
                if (num % key == 0) {
                    numAnsStr += fizzBizzDict.get(key);
                }
            }

            if (numAnsStr.equals("")) {
                // Not divisible by 3 or 5, add the number
                numAnsStr += Integer.toString(num);
            }

            // Append the current answer str to the ans list
            ans.add(numAnsStr);
        }

        return ans;
    }

    public static void main(String[] args) {
        Solution412FizzBuzz solution = new Solution412FizzBuzz();
        System.out.println(solution.fizzBuzz(20).toString());
    }
}
