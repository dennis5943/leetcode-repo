"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

 
Constraints:
	intervals[i][0] <= intervals[i][1]


"""
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        isInclude = lambda v,b: b[0] <= v and v <= b[1]
        intervals.sort(key=lambda x: x[0])
        tmpBound = None
        res = []
        
        for interval in intervals:
            if not tmpBound:
                tmpBound = [interval[0],interval[1]]
            elif isInclude(interval[0],tmpBound):
                tmpBound[1] = max(interval[1] , tmpBound[1])
            else:
                res.append(tmpBound)
                tmpBound = interval

        if tmpBound:
            res.append(tmpBound)
        return res


if __name__ == '__main__':
    assert Solution().merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert Solution().merge([[1,4],[4,5]]) == [[1,5]]
    assert Solution().merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert Solution().merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]

