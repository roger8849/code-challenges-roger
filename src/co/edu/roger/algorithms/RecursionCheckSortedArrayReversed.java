package co.edu.roger.algorithms;

public class RecursionCheckSortedArrayReversed {
    /**
     *
     * @param A Array to check
     * @param startIndex index to check elements
     * @param n number of elements into de array.
     * @return
     */
    public boolean isSorted(int A[], int startIndex, int n) {
        // Base case. If no elements or single elements the array is sorted.
        if( n==0|| n==1  ) {
            return true;
        }

        if(A[startIndex-1] <= A[startIndex]) {
            //  1 less element to check in the array.
            boolean smallAnswer = isSorted(A, startIndex - 1, n-1);
            return smallAnswer;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        RecursionCheckSortedArrayReversed recursionCheckSortedArray = new RecursionCheckSortedArrayReversed();
        int []example1 = {1,2,3,4,5,6,32,100};
        System.out.println("Example 1 is sorted? " + recursionCheckSortedArray.isSorted(example1, example1.length-1, example1.length));

        int []example2 = {10,2,3,4,50,6};
        System.out.println("Example 2 is sorted? " + recursionCheckSortedArray.isSorted(example2, example2.length-1, example2.length));


    }
}
