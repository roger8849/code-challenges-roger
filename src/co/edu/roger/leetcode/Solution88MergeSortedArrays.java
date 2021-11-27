package co.edu.roger.leetcode;

import java.util.Arrays;

/**
 * Merge Sorted Array
 * <p>
 * Solution
 * You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
 * <p>
 * Merge nums1 and nums2 into a single array sorted in non-decreasing order.
 * <p>
 * The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
 * <p>
 * <p>
 * <p>
 * Example 1:
 * <p>
 * Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
 * Output: [1,2,2,3,5,6]
 * Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
 * The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
 * Example 2:
 * <p>
 * Input: nums1 = [1], m = 1, nums2 = [], n = 0
 * Output: [1]
 * Explanation: The arrays we are merging are [1] and [].
 * The result of the merge is [1].
 * Example 3:
 * <p>
 * Input: nums1 = [0], m = 0, nums2 = [1], n = 1
 * Output: [1]
 * Explanation: The arrays we are merging are [] and [1].
 * The result of the merge is [1].
 * Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 * <p>
 * <p>
 * Constraints:
 * <p>
 * nums1.length == m + n
 * nums2.length == n
 * 0 <= m, n <= 200
 * 1 <= m + n <= 200
 * -109 <= nums1[i], nums2[j] <= 109
 * <p>
 * <p>
 * Follow up: Can you come up with an algorithm that runs in O(m + n) time?
 */
public class Solution88MergeSortedArrays {

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        System.out.println(Arrays.toString(nums1) + " " + Arrays.toString(nums2));
        // Length of first array
        int i = m + n - 1;
        // While I should copy elements.
        while (i >= 0) {
            boolean hasNums1LeftNext = m > 0;
            boolean hasNums2LeftNext = n > 0;
            // Both arrays still have elements.
            if (hasNums1LeftNext && hasNums2LeftNext) {
                if(nums1[m-1] > nums2[n-1]){
                    nums1[i] = nums1[m-1];
                    m--;
                } else {
                    nums1[i] = nums2[n-1];
                    n--;
                }
            // Just nums1 has elements
            } else if (hasNums1LeftNext) {
                while (hasNums1LeftNext && i >= 0) {
                    nums1[i] = nums1[m-1];
                    m--; i--;
                    hasNums1LeftNext = m > 0;
                }
            // Just nums2 has elements
            } else if (hasNums2LeftNext) {
                while (hasNums2LeftNext && i >= 0) {
                    nums1[i] = nums2[n-1];
                    n--; i--;
                    hasNums2LeftNext = n > 0;
                }
            }
            i--;
        }
        System.out.println(Arrays.toString(nums1));
    }

    public static void main(String[] args) {
        Solution88MergeSortedArrays solution = new Solution88MergeSortedArrays();
        int nums1[] = {1, 2, 3, 0, 0, 0}, m = 3, nums2[] = {2, 5, 6}, n = 3;
        solution.merge(nums1, m, nums2, n);
        int nums3[] = {1}, m2 = 1, nums4[] = {}, n2 = 0;
        solution.merge(nums3, m2, nums4, n2);
        int nums5[] = {0}, m3 = 0, nums6[] = {1}, n3 = 1;
        solution.merge(nums5, m3, nums6, n3);

    }
}
