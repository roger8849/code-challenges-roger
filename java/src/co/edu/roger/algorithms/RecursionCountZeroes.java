package co.edu.roger.algorithms;

import java.util.Scanner;

/**
 * Objective: count the 0s in a number recursively.
 */
public class RecursionCountZeroes {

    private static final Scanner scanner = new Scanner(System.in);

    public int countZeroes(long n) {
        //base case
        if (n <= 0) {
            return 0;
        }
        // recursive call n/10 cuts the integer in 1 digit
        int smallAns = countZeroes(n / 10);

        //calculation
        long lastDigit = n % 10;
        if (lastDigit == 0) {
            return smallAns + 1;
        } else {
            return  smallAns;
        }
    }

    public static void main(String[] args) {
        long n = scanner.nextLong();
        while (n <= 0) {
            System.out.println("Integer must be greater than 0");
            n = scanner.nextLong();
        }
        RecursionCountZeroes recursionCountZeroes = new RecursionCountZeroes();
        System.out.println("number of zeroes of n: " + recursionCountZeroes.countZeroes(n));
    }
}
