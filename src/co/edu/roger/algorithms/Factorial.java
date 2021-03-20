package co.edu.roger.algorithms;

import java.util.Scanner;

public class Factorial {
    public int factorial(int n) {
        if(n > 0) {
            return n * factorial(n-1);
        } else {
            return 1;
        }
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        Factorial factorial = new Factorial();
        int n = scanner.nextInt();
        System.out.println("factorial 5: " + factorial.factorial(n));
    }
}
