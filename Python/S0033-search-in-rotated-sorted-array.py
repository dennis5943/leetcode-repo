"""
Given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You should search for target in nums and if you found return its index, otherwise return -1.

 
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:
Input: nums = [1], target = 0
Output: -1

 
Constraints:
	1 <= nums.length <= 5000
	-10^4 <= nums[i] <= 10^4
	All values of nums are unique.
	nums is guranteed to be rotated at some pivot.
	-10^4 <= target <= 10^4


"""
from typing import List
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		k=0
		
		for i in range(len(nums) - 1):
			if nums[i] > nums[i+1]:
				k = i + 1
		
		orgnums = nums[k:] + nums[:k]

		def binarySearch(start,end):
			if end == start:
				return start if orgnums[start] == target else -1

			mid = int( (end + start) / 2 )
			midval = orgnums[mid]

			if midval == target:
				return mid
			elif midval > target:
				return binarySearch(start,max(start,mid - 1))
			else:
				return binarySearch(min(end,mid + 1) , end)
		
		tgtidx = binarySearch(0,len(orgnums) - 1)
		tgtidx = (tgtidx + k)%len(nums) if tgtidx >= 0 else -1
		
		return tgtidx

if __name__ == '__main__':
	assert Solution().search([3,1],3) == 0
	assert Solution().search([1,3],1) == 0
	assert Solution().search([1,3],0) == -1
	assert Solution().search([1],0) == -1
	assert Solution().search([4,5,6,7,0,1,2],0) == 4
	assert Solution().search([4,5,6,7,0,1,2],3) == -1