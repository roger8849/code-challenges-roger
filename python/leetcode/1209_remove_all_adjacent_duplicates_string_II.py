'''
1209. Remove All Adjacent Duplicates in String II
Medium

Share
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

Constraints:

1 <= s.length <= 105
2 <= k <= 104
s only contains lower case English letters.
'''

class Solution:

    # O(n) iterate the string 1 time
    # S(n) create a stack to store elements
    def removeDuplicates(self, s: str, k: int) -> str:
        string_stack = list()
        result = str()

        for letter in s :
            # If the stack doesn't have elements push and count is one
            if not string_stack:
                string_stack.append([letter, 1])
            else:
                # Get the top element.
                key, count = string_stack.pop()
                # if the top element is the current letter
                if letter == key:
                    # increase its count
                    count += 1
                    # if the count is == k then do not insert the element again
                    if count != k:
                        string_stack.append([letter, count])
                else:
                    # insert the previous top element
                    string_stack.append([key, count])
                    # inser the new top element
                    string_stack.append([letter, 1])

        # Join together the string.
        for key, count in string_stack:
            while(count > 0):
                result += key
                count -= 1
        return result

def main():
    solution = Solution()
    print(solution.removeDuplicates(s = "abcd", k = 2))
    print(solution.removeDuplicates(s = "deeedbbcccbdaa", k = 3))
    print(solution.removeDuplicates(s = "pbbcggttciiippooaais", k = 2))

if __name__ == "__main__":
    main()