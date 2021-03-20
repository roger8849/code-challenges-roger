package co.edu.roger.algorithms;

import java.util.Scanner;

public class Fibonacci {
    public int fibonacci(int n) {
        if( n == 0)// 1st base case no. 1
            return 0;
        if( n == 1 ) // 1st base case no. 2
            return 1;

        int smallAns1 = fibonacci(n - 1); // 2nd. step recursion keys Induction hypothesis 1
        int smallAns2 = fibonacci(n - 2); // 2nd. step recursion keys. Induction hypothesis 2

        return smallAns1 + smallAns2; // 3rd. Induction step.

    }
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        Fibonacci fibonacci = new Fibonacci();
        int n = scanner.nextInt();
        System.out.println("Fibonacci of n=" + n + " is " + fibonacci.fibonacci(n));
    }
}
