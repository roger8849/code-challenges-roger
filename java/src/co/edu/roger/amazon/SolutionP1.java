package co.edu.roger.amazon;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;
import java.util.stream.IntStream;

import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class SolutionP1 {

    static class Result {

        /*
         * Complete the 'minimalHeaviestSetA' function below.
         *
         * The function is expected to return an INTEGER_ARRAY.
         * The function accepts INTEGER_ARRAY arr as parameter.
         */

        public static List<Integer> minimalHeaviestSetA(List<Integer> arr) {
            Stack<Integer> A = new Stack<>();
            //arr = arr.stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList());
            Collections.sort(arr, Collections.reverseOrder());
            int totalSum = 0;
            int ASum = 0;
            // Calculating the sum of all the elements of array
            for (Integer element : arr) {
                totalSum += element;
            }
            // index of array
            int index = 0;
            while (index < arr.size()) {
                int nextElementOfArr = arr.get(index);
                A.push(nextElementOfArr);
                ASum += nextElementOfArr;
                int rest = totalSum - ASum;
                // found the minimal
                if (ASum - rest > 0) {
                    break;
                }
                index++;
            }
            return new ArrayList<>(A);
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("/Users/i864532/GitHub/code-challenges-roger/out/solution1.txt"));


        int arrCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = IntStream.range(0, arrCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                .map(String::trim)
                .map(Integer::parseInt)
                .collect(toList());

        List<Integer> result = Result.minimalHeaviestSetA(arr);

        bufferedWriter.write(
                result.stream()
                        .map(Object::toString)
                        .collect(joining("\n"))
                        + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}
