package co.edu.roger.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

/**
 * Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
 *
 *
 *
 * Example 1:
 *
 * Input: nums = [-4,-1,0,3,10]
 * Output: [0,1,9,16,100]
 * Explanation: After squaring, the array becomes [16,1,0,9,100].
 * After sorting, it becomes [0,1,9,16,100].
 * Example 2:
 *
 * Input: nums = [-7,-3,2,3,11]
 * Output: [4,9,9,49,121]
 *
 *
 * Constraints:
 *
 * 1 <= nums.length <= 104
 * -104 <= nums[i] <= 104
 * nums is sorted in non-decreasing order.
 *
 *
 * Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
 */
public class Solution977SquaresofaSortedArray {

    /**
     * O(n)
     * S(n)
     *
     * @param nums
     * @return
     */
    public int[] sortedSquares(int[] nums) {
        int sortedSquares[] = new int[nums.length];
        int start = 0;
        int end = nums.length - 1;

        // Index of insertion

        int j = nums.length - 1;

        // two pointers because array is sorted.
        while(start <= end && j>=0){
            int startPow = (int) Math.pow(nums[start], 2);
            int endPow = (int) Math.pow(nums[end],2);
            // comparing pows.
            if(startPow >= endPow){
                sortedSquares[j] = startPow;
                start++;
            } else {
                sortedSquares[j] = endPow;
                end--;
            }
            j--;
        }
        return sortedSquares;
    }

    public static void main(String[] args) {
        Solution977SquaresofaSortedArray solution = new Solution977SquaresofaSortedArray();
        int nums1[] = {-4,-1,0,3,10};
        System.out.println(Arrays.toString(solution.sortedSquares(nums1)));
    }
}
