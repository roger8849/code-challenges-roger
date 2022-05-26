package co.edu.roger.amazon;

import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

//import jdk.jshell.SourceCodeAnalysis;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class SolutionKeywordSuggester {

    static class Result {
        /*
         * Complete the 'searchSuggestions' function below.
         *
         * The function is expected to return a 2D_STRING_ARRAY.
         * The function accepts following parameters:
         *  1. STRING_ARRAY repository
         *  2. STRING customerQuery
         */
        public static List<List<String>> searchSuggestions(List<String> repository, String customerQuery) {
            // Write your code here
            List<List<String>> result = new ArrayList<>();
            for (int i = 2; i <= customerQuery.length(); i++) {
                String searchTerm = customerQuery.substring(0, i);
                searchTerm.toLowerCase();
                List<String> foundwords = searchSuggestionForSubstr(repository, searchTerm);
                if(foundwords != null){
                    result.add(foundwords);
                }
            }
            return result;
        }

        private static List<String> searchSuggestionForSubstr(List<String> repository, String searchTerm) {
            List<String> terms = new ArrayList<>();
            terms = repository.stream().filter(word -> {
                        word.toLowerCase();
                        return word.startsWith(searchTerm);
                    }
            ).sorted().limit(3).collect(Collectors.toList());
            return terms;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        //BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("/Users/i864532/GitHub/code-challenges-roger/out/solution_keywordSuggester.txt"));

        int repositoryCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> repository = IntStream.range(0, repositoryCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
                .collect(toList());

        String customerQuery = bufferedReader.readLine();

        List<List<String>> result = Result.searchSuggestions(repository, customerQuery);

        result.stream()
                .map(
                        r -> r.stream()
                                .collect(joining(" "))
                )
                .map(r -> r + "\n")
                .collect(toList())
                .forEach(e -> {
                    try {
                        bufferedWriter.write(e);
                    } catch (IOException ex) {
                        throw new RuntimeException(ex);
                    }
                });

        bufferedReader.close();
        bufferedWriter.close();
    }

}
