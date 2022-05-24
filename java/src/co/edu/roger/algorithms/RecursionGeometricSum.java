package co.edu.roger.algorithms;

import java.util.Scanner;

/**
 * Objective: given n sum 1 + 1/2^1 + 1/2^2 + ... + 1/2^n
 */
public class RecursionGeometricSum {
    public double recursionSum(int n) {
        // base case
        if(n == 0) {
            return 1;
        }

        // recursive call
        double smallAns = recursionSum(n-1);

        //operation
        return smallAns + 1.0/Math.pow(2,n);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        RecursionGeometricSum recursionGeometricSum = new RecursionGeometricSum();
        int n = scanner.nextInt();
        System.out.println("geometric sum: " + recursionGeometricSum.recursionSum(n));
    }
}
