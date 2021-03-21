package co.edu.roger.codility;

import java.util.*;

/*

* This is a demo task.
*
* Write a function:
*
* class Solution { public int solution(int[] A); }
*
* that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
*
* For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
*
* Given A = [1, 2, 3], the function should return 4.
*
* Given A = [−1, −3], the function should return 1.
*
* Write an efficient algorithm for the following assumptions:
*
* N is an integer within the range [1..100,000];
* each element of array A is an integer within the range [−1,000,000..1,000,000].
 */
public class SolutionDemoCodility {

    public int solution(int[] A) {
        // write your code in Java SE 8
        Set<Integer> integers =  new HashSet<>();
        Collections.addAll(integers, Arrays.stream(A).boxed().toArray(Integer[]::new));
        int i = 1;
        for ( ; i < A.length + 1; i++) {
            if (!integers.contains(i)) {
                return i;
            }
        }
        return i;

    }

    public static void main(String[] args) {
        int A[] = {1, 3, 6, 4, 1, 2};
        SolutionDemoCodility solutionDemoCodility = new SolutionDemoCodility();
        System.out.println(solutionDemoCodility.solution(A));

        int A1[] = {1,2,3};
        System.out.println(solutionDemoCodility.solution(A1));
        int A2[] = {-1, -3};
        System.out.println(solutionDemoCodility.solution(A2));
    }
}
