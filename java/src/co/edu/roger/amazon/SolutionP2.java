package co.edu.roger.amazon;

import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

public class SolutionP2 {

    static class Result {

        /*
         * Complete the 'numberOfItems' function below.
         *
         * The function is expected to return an INTEGER_ARRAY.
         * The function accepts following parameters:
         *  1. STRING s
         *  2. INTEGER_ARRAY startIndices
         *  3. INTEGER_ARRAY endIndices
         */

        public static List<Integer> numberOfItems(String s, List<Integer> startIndices, List<Integer> endIndices) {
            // Write your code here
            List<Integer> itemsInContainers = new ArrayList<>();
            for (int i = 0; i < startIndices.size(); i++) {
                int startIdx = startIndices.get(i) - 1;
                int endIdx = endIndices.get(i) - 1;
                int elements = getElementsFromString(s, startIdx, endIdx);
                itemsInContainers.add(elements);

            }
            return itemsInContainers;
        }

        public static Integer getElementsFromString(String s, int startIdx, int endIdx) {
            // Look for the string to analise
            s = s.substring(startIdx, endIdx);
            int firstIndex = s.indexOf('|');
            int lastIndex = s.lastIndexOf('|');
            s = s.substring(firstIndex, lastIndex);
            s = s.replaceAll("|","" );
            return s.length();

//            for (int i = startIdx; i <= endIdx; i++) {
//                int tempCount = 0;
//                char item = s.charAt(i);
//                // opened
//                if (item == '|') {
//                    i++;
//                    item = s.charAt(i);
//                }
//                while (item == '*' && i < s.length()) {
//                    item = s.charAt(i);
//                    i++;
//                    tempCount++;
//                }
//                // closed
//                if (item == '|') {
//                    totalElements += tempCount;
//                }
//            }
//            return totalElements;
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("/Users/i864532/GitHub/code-challenges-roger/out/solution1.txt"));


        String s = bufferedReader.readLine();

        int startIndicesCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> startIndices = IntStream.range(0, startIndicesCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                .map(String::trim)
                .map(Integer::parseInt)
                .collect(toList());

        int endIndicesCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> endIndices = IntStream.range(0, endIndicesCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                .map(String::trim)
                .map(Integer::parseInt)
                .collect(toList());

        List<Integer> result = Result.numberOfItems(s, startIndices, endIndices);

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
