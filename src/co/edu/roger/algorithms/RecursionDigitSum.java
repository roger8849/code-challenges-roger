package co.edu.roger.algorithms;

import java.util.Scanner;

/**
 * Objective: count the number of digitis recursively
 */
public class RecursionDigitSum {

    private static final Scanner scanner = new Scanner(System.in);

    public int sumDigits(int n) {
        //base case
        if (n <= 0) {
            return 0;
        }
        // recursive call n/10 cuts the integer in 1 digit
        int smallAns = sumDigits(n / 10);

        //calculation
        int lastDigit = n % 10;
        return smallAns + lastDigit;
    }

    public static void main(String[] args) {
        int n = scanner.nextInt();
        while (n <= 0) {
            System.out.println("Integer must be greater than 0");
            n = scanner.nextInt();
        }
        RecursionDigitSum recursionDigitSum = new RecursionDigitSum();
        System.out.println("number of digits of n: " + recursionDigitSum.sumDigits(n));
    }
}
