"""
Given an array of integers nums and a positive integer k, find whether it&#39;s possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It&#39;s possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

 

Note:
	1 <= k <= len(nums) <= 16.
	0 < nums[i] < 10000.


"""
from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().canPartitionKSubsets(0) == 0

