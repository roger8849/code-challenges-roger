package co.edu.roger.codility;

import java.util.Scanner;

/*

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at
both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary
representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary
representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no
binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

class Solution { public int solution(int N); }

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N
doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its
longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation
'100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
 */
public class SolutionBinaryGaps {

    private static final Scanner scanner = new Scanner(System.in);

    public int solution(final int N) {
        String binaryRepresentation = Integer.toBinaryString(N);
        final int representationLength = binaryRepresentation.length();
        if (representationLength < 3) {
            return 0;
        }
        int binaryGap = 0;
        int currentCount = 0;
        boolean counting;
        // Go through the array
        for (int i = 1; i < representationLength; i++) {
            if (binaryRepresentation.charAt(i - 1) == '1' && binaryRepresentation.charAt(i) == '0') {
                counting = true;
                currentCount++;
                i++;
                // Advance and count the gap until is over or the array finished.
                while (counting && i < representationLength) {
                    // Is still a gap
                    if (binaryRepresentation.charAt(i - 1) == '0' && binaryRepresentation.charAt(i) == '0') {
                        currentCount++;
                        i++;
                    } else { // Gap is over and the array hasn't finished
                        counting = false;
                        binaryGap = currentCount > binaryGap ? currentCount : binaryGap;
                        currentCount = 0;
                    }
                }
            }
        }
        return binaryGap;
    }

    public static void main(String[] args) {
        final int input = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        SolutionBinaryGaps solutionBinaryGaps = new SolutionBinaryGaps();


        System.out.println("Solution:" + solutionBinaryGaps.solution(input));
    }
}
