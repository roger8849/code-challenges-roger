package co.edu.roger.hacerrank;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class SolutionCountingValleys {

	private static final Scanner scanner = new Scanner(System.in);

	// Complete the countingValleys function below.
	static int countingValleys(int n, String s) {
		int valleys = 0;
		int mountains = 0;
		int generalCount = 0;
		int previousStep = 0;
		char[] chars = s.toCharArray();
		for (int i = 0; i < chars.length ; i++ ){
			previousStep = generalCount;
			if(chars[i] == 'U'){
				generalCount++;
			} else {
				generalCount--;
			}
			if(generalCount == 0 && previousStep !=0){
				if(previousStep > 0){
					mountains++;
				} else{
					valleys++;
				}
			}
		}
		System.out.println("Valleys: " + valleys);
		System.out.println("Mountains: " + mountains);
		return valleys;
	}

	public static void main(String[] args) throws IOException {
		//BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
		BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("/Users/i864532/personal-shit-projects/out/output_path/solution_counting_valleys.txt"));


		int n = scanner.nextInt();
		scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

		String s = scanner.nextLine();

		int result = countingValleys(n, s);

		bufferedWriter.write(String.valueOf(result));
		bufferedWriter.newLine();

		bufferedWriter.close();

		scanner.close();
	}
}
