'''
1854. Maximum Population Year
Easy

Share
You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

Return the earliest year with the maximum population.

 

Example 1:

Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.
Example 2:

Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation: 
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.
 

Constraints:

1 <= logs.length <= 100
1950 <= birthi < deathi <= 2050
Accepted
38,561
Submissions
64,668
'''

from typing import List, OrderedDict
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        yearsDict = OrderedDict()
        ans, maxPopulation = None, None
        # Years count
        for log in logs:
            born, death = log[0], log[1]
            # if born +1 if death -1 
            yearsDict[born] = yearsDict[born] + 1 if born in yearsDict else 1
            yearsDict[death] = yearsDict[death] - 1 if death in yearsDict else -1

        currentPeople = 0
        for year in sorted(yearsDict.keys()):
            if not ans:
                ans = year
                maxPopulation = yearsDict[year]
                currentPeople = yearsDict[year]
            else:
                currentPeople += yearsDict[year]
                if currentPeople > maxPopulation:
                    maxPopulation = currentPeople
                    ans = year
        return ans

def main():
    solution = Solution()
    ans = solution.maximumPopulation([[1993,1999],[2000,2010]]) 
    assert ans == 1993
    ans = solution.maximumPopulation([[1950,1961],[1960,1971],[1970,1981]])
    assert ans == 1960
    ans = solution.maximumPopulation([[1982,1998],[2013,2042],[2010,2035],[2022,2050],[2047,2048]])
    assert ans == 2022

if __name__ == "__main__":
    main()