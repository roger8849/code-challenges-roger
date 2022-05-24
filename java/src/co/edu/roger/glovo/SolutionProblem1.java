package co.edu.roger.glovo;

public class SolutionProblem1 {
    /**
     *
     *
     * @param A
     * @param targetAverage
     * @return
     */
    public boolean averagePair(int[] A, double targetAverage) {
        int startIdx = 0;
        int endIdx = A.length - 1;
        while (startIdx < endIdx) {
            double average = (A[startIdx] + A[endIdx]) / 2.0;
            if( average > targetAverage) {
                endIdx--;
            } else if( average < targetAverage ) {
                startIdx++;
            } else { // they are equal
                return true;
            }
        }
        return false;
    }
    // S(1) -> O(n)
    public static void main(String[] args) {
        SolutionProblem1 solution = new SolutionProblem1();
        int[] example1 = {1, 2, 3};
        System.out.println("has average pair: " + solution.averagePair(example1, 2.5));

        int[] example2 = {1, 3, 3, 5, 6, 7, 10, 12, 19};
        System.out.println("has average pair: " + solution.averagePair(example2, 8));

        int[] example3 = {-1, 0, 3, 4, 5, 6};
        System.out.println("has average pair: " + solution.averagePair(example3, 4.1));

        int[] example4 = {};
        System.out.println("has average pair: " + solution.averagePair(example4, 4));

        int[] example5 = {0, 2, 3};
        System.out.println("has average pair: " + solution.averagePair(example5, 2.0));

        int[] example6 = {0, 2, 4};
        System.out.println("has average pair: " + solution.averagePair(example6, 2.0));

    }

    /*

[1, 2, 3], 2.5 -> true
[1, 3, 3, 5, 6, 7, 10, 12, 19], 8 -> true
[-1, 0, 3, 4, 5, 6], 4.1 -> false
[], 4 -> false
[0, 2, 3], 2.0 -> false
[0, 2, 4], 2.0 -> true

*/
}
