package co.edu.roger.codility;

import java.util.Arrays;
import java.util.Scanner;

/*
    An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one
    index, and the last element of the array is moved to the first place. For example, the rotation of array
    A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

    The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

    Write a function:

    class Solution { public int[] solution(int[] A, int K); }

    that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

    For example, given

        A = [3, 8, 9, 7, 6]
        K = 3
    the function should return [9, 7, 6, 3, 8]. Three rotations were made:

        [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
        [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
        [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
    For another example, given

        A = [0, 0, 0]
        K = 1
    the function should return [0, 0, 0]

    Given

        A = [1, 2, 3, 4]
        K = 4
    the function should return [1, 2, 3, 4]

    Assume that:

    N and K are integers within the range [0..100];
    each element of array A is an integer within the range [−1,000..1,000].
    In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
 */
public class Solution02CyclicRotation {

    private static final Scanner scanner = new Scanner(System.in);

    public int[] solution(int[] A, int K){

        int rotatedArray[] = new int[A.length];
        for (int i = 0; i < A.length; i++) {
            int rotatedPosition = (K + i) % A.length;
            rotatedArray[rotatedPosition] = A[i];
        }
        return rotatedArray;
    }

    public static void main(String[] args) {
//        final int input = scanner.nextInt();
//        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        Solution02CyclicRotation solution02CyclicRotation = new Solution02CyclicRotation();
        final int A[] = {3, 8, 9, 7, 6};
        final int K = 3;
        System.out.println(Arrays.toString(solution02CyclicRotation.solution(A, K)));


        //System.out.println("Solution:" + solution02CyclicRotation.solution(input));
    }
}
