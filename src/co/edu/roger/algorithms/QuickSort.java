package co.edu.roger.algorithms;

import java.util.Arrays;

public class QuickSort {
    public int partition(int array[], int lowerBound, int upperBound){
        int pivot= array[lowerBound];
        int start = lowerBound;
        int end = upperBound;
        while (start < end) {
            // TODO fix with array of two elements.
            while (array[start] <= pivot) {
                start++;
            }
            while (array[end] > pivot){
                end--;
            }
            if(start < end){
               int temp = array[start];
               array[start] = array[end];
               array[end] = temp;
            }
        }
        int temp = array[lowerBound];
        array[lowerBound] = array[end];
        array[end] = temp;
        return end;
    }

    public void quickSort(int array[], int lowerBound, int upperBound) {
        if(lowerBound < upperBound) {
            int location = partition(array, lowerBound, upperBound);
            quickSort(array, lowerBound, location-1);
            quickSort(array, location +1, upperBound);
        }
    }

    public static void main(String[] args) {
        QuickSort quickSort = new QuickSort();
        int example1[] = {4,25,72,2,1,90,67,23,1,0,-1};
        quickSort.quickSort(example1, 0, example1.length-1);
        System.out.println(Arrays.toString(example1));

        int example2[] = {4};
        quickSort.quickSort(example2, 0, example2.length-1);
        System.out.println(Arrays.toString(example2));

        int example3[] = {4,2};
        quickSort.quickSort(example3, 0, example3.length-1);
        System.out.println(Arrays.toString(example3));
    }
}
