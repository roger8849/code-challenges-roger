package co.edu.roger.algorithms;

import java.util.Arrays;

public class SearchAlgorithms {

    /**
     * Strategy for non sorted arrays.
     * O(n)
     *
     * @param a
     * @param key
     * @return -1 if not found, index of the element in array a.
     */
    private int linearSearch(int a[], int key) {

        for (int i = 0; i < a.length; i++) {
            if (a[i] == key) {
                return i;
            }
        }

        // Index not found
        return -1;
    }

    /**
     * Strategy ONLY for sorted arrays.
     * <p>
     * O(log n)
     *
     * @param a
     * @param key
     * @return -1 if not found, index of the element in array a.
     */
    private int binarySearch(int a[], int key, int start, int end) {

        // Element not found.
        if (start > end) {
            return -1;
        }
        int mid = (start + end) / 2;

        //element found
        if (a[mid] == key) {
            return mid;
            // Element should be in the first half of the array.
        } else if (a[mid] > key) {
            end = mid - 1;
            return binarySearch(a, key, start, end);
            // Element should be in the second half of the array
        } else {
            start = mid + 1;
            return binarySearch(a, key, start, end);
        }

    }

    /**
     *
     * @param args
     */
    public static void main(String[] args) {
        SearchAlgorithms searchAlgorithms = new SearchAlgorithms();

        int a[] = {10, 22, 13, 42, 56, 6};
        int index = searchAlgorithms.linearSearch(a, 56);
        if (index == -1) {
            System.out.println("Linear search: Index not found");
        } else {
            System.out.println("Linear search: Index found at: " + index);
        }

        int b[] = {1, 5, 10, 13, 22, 23, 42, 56, 55, 65, 68, 78};
        index = searchAlgorithms.binarySearch(b, 78, 0, b.length - 1);
        if (index == -1) {
            System.out.println("Binary search: Index not found");
        } else {
            System.out.println("Binary search: Index found at: " + index);
        }

    }
}
