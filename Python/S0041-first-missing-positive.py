"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Follow up:
Your algorithm should run in O(n) time and uses constant extra space.

"""
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minv = 2**31 - 1
        maxv = 0
        cnt = 0
        tmpset = set()
        for num in nums:
            if num <= 0 :
                continue

            minv = min(minv,num)
            maxv = max(num,maxv)
            cnt += 1
            tmpset.add(num)
        
        if minv > 1:
            return 1

        totalSet = set(range(minv,maxv+1)) - tmpset
        if not any(totalSet):
            return maxv + 1
        elif any(totalSet):
            llist = list(totalSet)
            mm = llist[0]
            for num in llist:
                mm = min(mm,num)
            return mm
        
        return 1


if __name__ == '__main__':
    assert Solution().firstMissingPositive([1,2,3,10,2147483647,9]) == 4
    assert Solution().firstMissingPositive([1,2,0]) == 3
    assert Solution().firstMissingPositive([3,4,-1,1]) == 2
    assert Solution().firstMissingPositive([7,8,9,11,12]) == 1

