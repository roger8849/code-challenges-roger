package co.edu.roger.algorithms;

import java.util.Scanner;

/**
 * Objective implement multiplication only adding numbers.
 */
public class RecursionMultiplication {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        RecursionMultiplication multiplication = new RecursionMultiplication();
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        System.out.println("Multiplication of " + m +" times " + n + " = " + multiplication.multiplication(m, n));
    }

    public int multiplication(int m, int n) {
        if(n == 0) return 0;
        if(n == 1) return m;
        return multiplication(m, n-1) + m;
    }
}
