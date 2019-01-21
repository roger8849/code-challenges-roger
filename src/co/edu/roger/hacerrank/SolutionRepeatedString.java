package co.edu.roger.hacerrank;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class SolutionRepeatedString {

	// Complete the repeatedString function below.
	static long repeatedString(String s, long n) {
		long totalOfAs = 0;
		long charLength = s.length();

		long repetitions = n/charLength;

		long asInSubstring = numberOfAsInSubstring(s);

		if (repetitions == 0){
			totalOfAs = numberOfAsInSubstring(s.substring(0, (int) n));
		} else{
			int mod = (int) (n % charLength);
			totalOfAs = asInSubstring * repetitions;
			if(mod != 0){
				String leftOverString = s.substring(0, mod);
				totalOfAs += numberOfAsInSubstring(leftOverString);
			}
		}
		System.out.println("Total of As: " + totalOfAs);
		return totalOfAs;

	}

	static int numberOfAsInSubstring(String s){
		int as = 0;
		char[] chars = s.toCharArray();
		for (int i = 0; i < chars.length; i++) {
			if( chars[i] == 'a' ){
				as++;
			}
		}
		return as;
	}

	private static final Scanner scanner = new Scanner(System.in);

	public static void main(String[] args) throws IOException {
		BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("/Users/i864532/personal-shit-projects/out/output_path/solution_repeated_string.txt"));
		//BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

		String s = scanner.nextLine();

		long n = scanner.nextLong();
		scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

		long result = repeatedString(s, n);

		bufferedWriter.write(String.valueOf(result));
		bufferedWriter.newLine();

		bufferedWriter.close();

		scanner.close();
	}

}
