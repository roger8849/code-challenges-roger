package co.edu.roger.algorithms;

import java.util.Scanner;

public class RecursionPrintRecursively {
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
        RecursionPrintRecursively recursionPrintRecursively = new RecursionPrintRecursively();
        int n = scanner.nextInt();
        recursionPrintRecursively.printRecursively(n);
    }
}
