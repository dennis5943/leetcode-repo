"""
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Constraints:
	0 <= nums.length <= 10^5
	-10^9 <= nums[i] <= 10^9
	nums is a non decreasing array.
	-10^9 <= target <= 10^9
"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(start,end):
            if end == start:
                return start if nums[start] == target else -1
            mid = int( (end + start) / 2 )
            midval = nums[mid]
            
            if midval == target:
                return mid
            elif midval > target:
                return binarySearch(start,max(start,mid - 1))
            else:
                return binarySearch(min(end,mid + 1) , end)

        if not any(nums):
            return [-1, -1]

        lb = binarySearch(0,len(nums) -1 )
        if lb >= len(nums) or nums[lb] != target:
            return [-1, -1]

        rang = [lb,lb]
        while 0 < rang[0] or rang[1] < len(nums) -1:
            if rang[0] -1 >= 0 and nums[lb] == nums[rang[0] -1]:
                rang[0] -= 1
            elif rang[1] + 1 < len(nums) and nums[lb] == nums[rang[1] + 1]:
                rang[1] += 1
            else:
                break
        return rang


if __name__ == '__main__':
    assert Solution().searchRange([2,2], 2) == [0, 1]
    assert Solution().searchRange([], 0) == [-1, -1]
    
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 5) == [0, 0]
    assert Solution().searchRange([1], 1) == [0, 0]