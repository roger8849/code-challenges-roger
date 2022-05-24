package co.edu.roger.leetcode;

/*
*
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
 */
public class Solution169MajorityElement {

    public int majorityElement(int[] nums) {
        // Moore's voting algorithm O(n) S(1)
        int count = 1;
        // Assuming the first element is the majority element.
        int majorityElement = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if(majorityElement == nums[i]) {
                count++;
            } else {
                count--;
            }
            if (count == 0) {
                majorityElement = nums[i];
                count = 1;
            }
        }
        return majorityElement;
    }

    public static void main(String[] args) {
        int example1[] = {2,2,1,1,1,2,2};
        int example2[] = {3,2,3};
        int example3[] = {2,2,1,1,4,4,4,4,4,4,4,4,4,4,1,2,2};
        Solution169MajorityElement solution = new Solution169MajorityElement();
        System.out.println(solution.majorityElement(example1));
        System.out.println(solution.majorityElement(example2));
        System.out.println(solution.majorityElement(example3));
    }
}
