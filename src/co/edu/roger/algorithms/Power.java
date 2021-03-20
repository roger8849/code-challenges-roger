package co.edu.roger.algorithms;

import java.util.Scanner;

public class Power {
    public int power(int x, int n) {
        if(n == 0) {// base case 1. never used.
            return 1;
        }
        if(n == 1) {// base case 2.
            return x;
        }

        return x * power(x, n-1);

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        Power power = new Power();
        int x = scanner.nextInt();
        int n = scanner.nextInt();
        System.out.println("Power of " + x +"^" + n + " = " + power.power(x, n));
    }
}
