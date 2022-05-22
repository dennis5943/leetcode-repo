"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],
-4 -1 -1 0 1 2

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        #print(nums,nums[:-2])
        #(a,b,c)
        for a_idx, a in enumerate(nums[:-2]):
            if a_idx >= 1 and a == nums[a_idx-1]:
                continue
            b_set = {}
            for c in nums[a_idx+1:]:
                if c not in b_set:
                    b_set[-a-c] = 1
                else:
                    res.add((a, -a-c, c))
        return list(res)


if __name__ == '__main__':
    
    print(Solution().threeSum([-1,0,1,2,-1,-4]))
