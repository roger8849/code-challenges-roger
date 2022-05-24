package co.edu.roger.hackerrank;

import java.io.*;
import java.util.*;

public class SolutionSockMerchant {

	// Complete the sockMerchant function below.
	static int sockMerchant(int n, int[] ar) {
		int pairs = 0;
		Map<Integer, Integer> pairsMap = new HashMap<>();

		for (int i = 0; i < ar.length; i++) {
			Integer color = ar[i];
			if(pairsMap.containsKey(color)){
				Integer colorCount = pairsMap.get(color);
				colorCount++;
				pairsMap.put(color, colorCount);
				if(colorCount % 2 == 0){
					pairs++;
				}
			} else {
				pairsMap.put(color, 1);
			}
		}

		return pairs;
	}

	private static final Scanner scanner = new Scanner(System.in);

	public static void main(String[] args) throws IOException {
		// BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

		BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("/Users/i864532/personal-shit-projects/out/output_path/solution_sock_merchant.txt"));


		int n = scanner.nextInt();
		scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

		int[] ar = new int[n];

		String[] arItems = scanner.nextLine().split(" ");
		scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

		for (int i = 0; i < n; i++) {
			int arItem = Integer.parseInt(arItems[i]);
			ar[i] = arItem;
		}

		int result = sockMerchant(n, ar);

		System.out.println("Result: " + result);

		bufferedWriter.write(String.valueOf(result));
		bufferedWriter.newLine();

		bufferedWriter.close();

		scanner.close();
	}
}
