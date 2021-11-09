package co.edu.roger.hackerrank;
import java.io.*;
import java.util.*;

public class SolutionArrayManipulation {
    // Complete the arrayManipulation function below.
    static long arrayManipulation(int n, int[][] queries) {
        long result = Long.MIN_VALUE;
        long[] progressiveArray = new long[n];
        Arrays.fill(progressiveArray, 0);
        for (int i = 0; i < queries.length ; i++) {
            int a = queries[i][0];
            int b = queries[i][1];
            int k = queries[i][2];
//            for (int j = a-1; j < b ; j++) {
//                progressiveArray[j] += k;
//                result = progressiveArray[j] > result ? progressiveArray[j] : result;
//            }
            progressiveArray[a-1] += k;
            if(b < n){
                progressiveArray[b]-=k;
            }
        }

        long temp=0;

        for (int i = 0; i <n ; i++) {
            temp += progressiveArray[i];
            if(temp > result){
                result = temp;
            }
        }

        System.out.println("Result: " + result);
        return result;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
//        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("C:\\Users\\roger\\IdeaProjects\\hackerrank-roger\\out\\output_path\\solution_ArrayManipulation.txt"));


        String[] nm = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nm[0]);

        int m = Integer.parseInt(nm[1]);

        int[][] queries = new int[m][3];

        for (int i = 0; i < m; i++) {
            String[] queriesRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 3; j++) {
                int queriesItem = Integer.parseInt(queriesRowItems[j]);
                queries[i][j] = queriesItem;
            }
        }

        long result = arrayManipulation(n, queries);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
