package co.edu.roger.geeksforgeeks;
//{ Driver Code Starts
//Initial Template for Java
import java.io.*;
import java.util.*;

/*
 * Pair in Java
EasyAccuracy: 67.28%Submissions: 3153Points: 2
Let's learn about Java Classes and how they can be useful.

Given an array A of N pairs of integers. The task is to sort the array on the basis of first element.

Hint: You may write a custom comparator. Read here.

Example 1:

Input:
3
1 2 5 4 3 6

Output:
1 2 3 6 5 4

Explanation:
Pairs are (1, 2), (5, 4), (3, 6). Sorting them on 
basis of first element, we have (1, 2), (3, 6), (5, 4).
Example 2:

Input:
2
4 8 2 24

Output:
2 24 4 8

Explanation:
Pairs are (4, 8), (2, 24). Sorting them on 
basis of first element, we have (2, 24),(4, 8).
Constraints:
1 <= N <= 104
1 <= A[i] <= 105
 */


//User function Template for Java
// Custom comparator class to sort the pairs
// on the basis of first element
class custom_Compare{
    
    // Compare function
    static void sortPairs(Pair arr[], int N){
        
        // Your code here
        Arrays.sort(arr, new SortbyFirst());
        
        //printing the x,y Pairs
        for(int i = 0;i<N;i++){
            System.out.print(arr[i].x + " " + arr[i].y + " ");
        }
        System.out.println();
    }
}

class SortbyFirst implements Comparator<Pair>{
    public int compare(Pair a, Pair b)
    {
        return a.x - b.x;
    }
}

public class PairInJava {
    // Driver code
	public static void main (String[] args) {
		
		//taking input using Scanner class 
		Scanner sc = new Scanner(System.in);
		
		//taking count of testcases
		int testcase = sc.nextInt();
		
		while(testcase-- > 0){
		    
		    //taking count of elements
		    int N = sc.nextInt();
		    
		    // Creating an array of Pair
		    Pair arr[] = new Pair[N];
		    
		    //adding elements to Pair array
		    for(int i = 0;i<N;i++){
		        int x = sc.nextInt();
		        int y = sc.nextInt();
		        arr[i] = new Pair(x, y);
		    }
		    
		    //creating an object of custom_Compare class
		    custom_Compare obj = new custom_Compare();
		    
		    //calling sortPairs() method of
		    //class  custom_Compare
		    obj.sortPairs(arr, N);
		}
	}
}

// Pair class
class Pair{
    int x;
    int y;
    
    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}
