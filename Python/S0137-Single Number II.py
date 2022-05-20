'''
137. Single Number II
Medium

4101

481

Add to List

Share
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        le = len(nums)
        if le == 1:
            return nums.pop()

        nums = sorted(nums)

        for i in range(0,le,3):
            #print(nums[i:i+3])
            tsub = nums[i:i+3]
            if len(tsub)==1:
                return tsub.pop()
            elif len(set(tsub)) == 1:
                continue
            elif len(set(tsub)) > 1:
                if tsub[0] == tsub[1]:
                    return tsub[2]
                elif tsub[1] == tsub[2]:
                    return tsub[0]
                else:
                    return tsub[1]
        return 0

if __name__ == '__main__':
    print('hello')
    print(Solution().singleNumber([2,2,3,2]))