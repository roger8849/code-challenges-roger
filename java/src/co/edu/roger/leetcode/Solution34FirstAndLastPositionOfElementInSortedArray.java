package co.edu.roger.leetcode;

/**
 * Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
 * <p>
 * If target is not found in the array, return [-1, -1].
 * <p>
 * You must write an algorithm with O(log n) runtime complexity.
 * <p>
 * <p>
 * <p>
 * Example 1:
 * <p>
 * Input: nums = [5,7,7,8,8,10], target = 8
 * Output: [3,4]
 * Example 2:
 * <p>
 * Input: nums = [5,7,7,8,8,10], target = 6
 * Output: [-1,-1]
 * Example 3:
 * <p>
 * Input: nums = [], target = 0
 * Output: [-1,-1]
 * <p>
 * <p>
 * Constraints:
 * <p>
 * 0 <= nums.length <= 105
 * -109 <= nums[i] <= 109
 * nums is a non-decreasing array.
 * -109 <= target <= 109
 */
public class Solution34FirstAndLastPositionOfElementInSortedArray {
    public int getFirst(int nums[], int target) {
        int start = 0, end = nums.length - 1;
        int answer = -1;
        while (start <= end) {
            int mid = (start + end) / 2;
            if(nums[mid] == target) {
                answer = mid;
                end = mid - 1;
                //return mid;
            } else if(nums[mid]< target) {
                start = mid+1;
            } else {
                end = mid - 1;
            }
        }
        return answer;
    }

    public int getLast(int nums[], int target){
        int start = 0, end = nums.length - 1;
        int answer = -1;
        while (start <= end) {
            int mid = (start + end) / 2;
            if(nums[mid] == target) {
                answer = mid;
                start = mid + 1;
                //return mid;
            } else if(nums[mid]< target) {
                start = mid+1;
            } else {
                end = mid - 1;
            }
        }
        return answer;
    }

    public int[] searchRange(int[] nums, int target) {
        int indexes[] = new int[2];
        int firstPos = getFirst(nums, target);
        int lastPos = -1;
        if(firstPos != -1){
            lastPos = getLast(nums, target);
        }
        indexes[0] = firstPos;
        indexes[1] = lastPos;
        return indexes;
    }

    public static void main(String[] args) {
        Solution34FirstAndLastPositionOfElementInSortedArray solution34FirstAndLastPositionOfElementInSortedArray = new Solution34FirstAndLastPositionOfElementInSortedArray();

        int nums[] = {5, 7, 7, 8, 8, 10}, target = 8;
        int[] indexes = solution34FirstAndLastPositionOfElementInSortedArray.searchRange(nums, target);
        System.out.println("Position of element: [" + indexes[0]+ ", " + indexes[1]+"]");


        int nums2[] = {5,7,7,8,8,10}, target2 = 6;
        indexes = solution34FirstAndLastPositionOfElementInSortedArray.searchRange(nums2, target2);
        System.out.println("Position of element: [" + indexes[0]+ ", " + indexes[1]+"]");

    }
}
