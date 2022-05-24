package co.edu.roger.amazon;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;

import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class SolutionFreshPromo {
    static class Result {

        /*
         * Complete the 'foo' function below.
         *
         * The function is expected to return an INTEGER.
         * The function accepts following parameters:
         *  1. STRING_ARRAY codeList
         *  2. STRING_ARRAY shoppingCart
         */

        public static int foo(List<String> codeList, List<String> shoppingCart) {
            // Write your code here
            int isWinner = 0;
            if (codeList == null || codeList.isEmpty()) {
                return 1;
            }
            List<String> codeWords = convertCodeListToSingleList(codeList);
            for (int i = 0; i < shoppingCart.size(); i++) {
                String cartElement = shoppingCart.get(i);
                int tempCartIdx = i;
                for (int j = 0; j < codeWords.size(); j++) {
                    String codeWord = codeWords.get(j);
                    if (codeWord.equalsIgnoreCase(cartElement) || "anything".equalsIgnoreCase(codeWord)) {
                        // Checking if is a winner
                        if (j + 1 == codeWords.size()) {
                            isWinner = 1;
                            return isWinner;
                        }
                        tempCartIdx++;
                        cartElement = shoppingCart.get(tempCartIdx);
                    }
                }
            }
            return isWinner;
        }

        public static List<String> convertCodeListToSingleList(List<String> codeList) {
            List<String> codeWords = new ArrayList<>();
            for (String code : codeList) {
                String[] codes = code.split(" ");
                for (String codeWord : codes) {
                    codeWords.add(codeWord);
                }
            }
            return codeWords;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        //BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("/Users/i864532/GitHub/code-challenges-roger/out/solution_freshPromo.txt"));

        int codeListCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> codeList = IntStream.range(0, codeListCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                .collect(toList());

        int shoppingCartCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> shoppingCart = IntStream.range(0, shoppingCartCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                .collect(toList());

        int result = Result.foo(codeList, shoppingCart);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }

}
