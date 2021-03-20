package co.edu.roger.algorithms;

import java.util.Scanner;

public class PrintRecursively {
    public void printRecursively(int n) {
        if( n == 0 ) return; // base case

        //Descending
//        System.out.println(n);
//        printRecursively(n-1);
        //Ascending
        printRecursively(n-1);
        System.out.println(n);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        PrintRecursively printRecursively = new PrintRecursively();
        int n = scanner.nextInt();
        printRecursively.printRecursively(n);
    }
}
