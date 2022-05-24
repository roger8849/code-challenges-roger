package co.edu.roger.algorithms;

import java.util.Scanner;

/**
 * Objective: count the number of digitis recursively
 */
public class RecursionDigitCount {

    private static final Scanner scanner = new Scanner(System.in);

    public int countDigits(int n) {
        //base case
        if (n <= 0) {
            return 0;
        }
        // recursive call n/10 cuts the integer in 1 digit
        int smallAns = countDigits(n / 10);

        //calculation
        return smallAns + 1;
    }

    public static void main(String[] args) {
        int n = scanner.nextInt();
        while (n <= 0) {
            System.out.println("Integer must be greater than 0");
            n = scanner.nextInt();
        }
        RecursionDigitCount recursionDigitCount = new RecursionDigitCount();
        System.out.println("number of digits of n: " + recursionDigitCount.countDigits(n));
    }
}
