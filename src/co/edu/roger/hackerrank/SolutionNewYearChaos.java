package co.edu.roger.hackerrank;
import java.util.*;

public class SolutionNewYearChaos {
    // Complete the minimumBribes function below.
    static void minimumBribes(int[] q) {
        boolean tooChaotic = false;
        int bribesTotal = 0;
        Map<Integer, Integer> peopleInLineMap = new HashMap<>();
        boolean isSorted = false;
        while(!isSorted){
            boolean checkAgain = false;
            for (int i = 0; i < q.length - 1; i++) {
                int briber = 0;
                if(q[i] > q[i+1]) {
                    checkAgain = true;
                    briber = q[i];
                    q[i] = q[i+1];
                    q[i+1] = briber;

                    if(peopleInLineMap.containsKey(briber)){
                        int bribesOfPerson = peopleInLineMap.get(briber) + 1;
                        if(bribesOfPerson > 2){
                            tooChaotic = true;
                            checkAgain = false;
                            break;
                        }
                        peopleInLineMap.put(briber, bribesOfPerson++);
                    } else{
                        peopleInLineMap.put(briber, 1);
                    }
                    bribesTotal++;
                }
                if(tooChaotic)
                    break;
            }
            if(!checkAgain)
                isSorted = true;
        }
        if (tooChaotic)
            System.out.println("Too chaotic");
        else
            System.out.println(bribesTotal);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[] q = new int[n];

            String[] qItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int i = 0; i < n; i++) {
                int qItem = Integer.parseInt(qItems[i]);
                q[i] = qItem;
            }

            minimumBribes(q);
        }

        scanner.close();
    }
}
