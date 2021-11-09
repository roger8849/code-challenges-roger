package co.edu.roger.hackerrank;

import java.io.*;
import java.util.*;

public class SolutionJumpingOnClouds {
	// Complete the jumpingOnClouds function below.
	static int jumpingOnClouds(int[] c) {
		int jumps = 0;

		for(int i = 0 ; i < c.length; ){
			int bigJump = i+2;
			int smallJump = i+1;
			if( bigJump < c.length && c[bigJump] == 0 ){
				i = bigJump;
				jumps++;
			} else if(smallJump < c.length) {
				i = smallJump;
				jumps++;
			} else {
				i++;
			}
		}
		System.out.println("Jumps: " + jumps);
		return jumps;
	}



	private static final Scanner scanner = new Scanner(System.in);

	public static void main(String[] args) throws IOException {
		//BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

		BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("/Users/i864532/personal-shit-projects/out/output_path/solution_jumping_on_clouds.txt"));


		int n = scanner.nextInt();
		scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

		int[] c = new int[n];

		String[] cItems = scanner.nextLine().split(" ");
		scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

		for (int i = 0; i < n; i++) {
			int cItem = Integer.parseInt(cItems[i]);
			c[i] = cItem;
		}

		int result = jumpingOnClouds(c);

		bufferedWriter.write(String.valueOf(result));
		bufferedWriter.newLine();

		bufferedWriter.close();

		scanner.close();
	}
}
