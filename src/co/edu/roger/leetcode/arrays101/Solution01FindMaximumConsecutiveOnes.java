package co.edu.roger.leetcode.arrays101;


/**
 * Given a binary array nums, return the maximum number of consecutive 1's in the array.
 *
 *
 *
 * Example 1:
 *
 * Input: nums = [1,1,0,1,1,1]
 * Output: 3
 * Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
 * Example 2:
 *
 * Input: nums = [1,0,1,1,0,1]
 * Output: 2
 */

public class Solution01FindMaximumConsecutiveOnes {
    public int naiveFindMaxConsecutiveOnes(int[] nums) {
        // 1s not found
        int value = 0;
        for (int i = 0; i < nums.length; i++) {
            int count = 0;
            while(i< nums.length && nums[i]==1 ) {
                count++;
                i++;
            }
            if(count > value)
                value = count;
        }
        return value;
    }

    public static void main(String[] args) {
        Solution01FindMaximumConsecutiveOnes solution01FindMaximumConsecutiveOnes = new Solution01FindMaximumConsecutiveOnes();
        int nums1[] =  {1,1,0,1,1,1};
        System.out.println(solution01FindMaximumConsecutiveOnes.naiveFindMaxConsecutiveOnes(nums1));

        int nums2[] = {1,0,1,1,0,1};
        System.out.println(solution01FindMaximumConsecutiveOnes.naiveFindMaxConsecutiveOnes(nums2));
    }
}
