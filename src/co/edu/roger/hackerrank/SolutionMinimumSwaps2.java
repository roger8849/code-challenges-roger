package co.edu.roger.hackerrank;
import java.io.*;
import java.util.*;

public class SolutionMinimumSwaps2 {


    // Complete the minimumSwaps function below.
    static int minimumSwaps(int[] arr) {
        int swaps = 0;
        int[] array = Arrays.copyOf(arr, arr.length), sortedArray = Arrays.copyOf(arr, arr.length);
        Arrays.sort(sortedArray);
        for (int i = 0; i < array.length; i++) {
            if(array[i] != sortedArray[i]){
                for (int j = i+1; j <array.length ; j++) {
                    if(array[j] == sortedArray[i]){
                        int temp = array[i];
                        array[i] = array[j];
                        array[j] = temp;
                        swaps++;
                        break;
                    }
                }
            }
        }

        System.out.println("Swaps: " + swaps);
        return swaps;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        //BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("C:\\Users\\roger\\IdeaProjects\\hackerrank-roger\\out\\output_path\\solution_minimumswaps2.txt"));


        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        int res = minimumSwaps(arr);

        bufferedWriter.write(String.valueOf(res));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
