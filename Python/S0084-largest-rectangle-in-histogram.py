"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 

The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10


"""
from collections import Counter
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #hashCnt = Counter(heights)
        #minHiehgt = min(hashCnt.keys())

        heights.append(0)
        stack = [-1]
        res = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                res = max(res, (height * width))
            stack.append(i)
        return res


if __name__ == '__main__':
    assert Solution().largestRectangleArea([2,1,2,1,2,1,6,6,1,3,1]) == 12
    assert Solution().largestRectangleArea([2,1,2]) == 3
    assert Solution().largestRectangleArea([9,0]) == 9
    assert Solution().largestRectangleArea([4,2]) == 4
    assert Solution().largestRectangleArea([2,1,5,6,2,3]) == 10
    assert Solution().largestRectangleArea([2,4]) == 4

