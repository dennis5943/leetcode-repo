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

        totalSet = set(range(minv,min(minv + cnt, maxv+1))) - tmpset
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

""" another better solution
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''Step 1 -> The main idea behind it is that the minimum number to be found will always be in the range [1....n]
		             where 'n' is the length of list. So keep numbers in this range and mark others
					 (here we are marking them with (n+1) value) in the list provided.'''
        
        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = n + 1
        
        '''Step 2 -> Ignoring the values greater than 'n', mark the indexes of the numbers in the range [1...n]
					 so as to ensure that this values are present. To mark the indexes, 
					 I am negating the value present at that index.'''
        
        for i in range(n):
            val = abs(nums[i])
            if val > n:
                continue
            val -= 1  #since the list is zero indexed,so every value will be at position val - 1
            
            if nums[val] > 0: 
                # For similar numbers, it will keep on fluctuating between negative and positive 
				# which is not our motive here.
                
                nums[val] = -1 * nums[val]
        
        '''Step 3 -> Return the first occurence of the non-negative numbers from the list'''
        
        for i in range(n):
            if nums[i] >=0:
                return (i + 1) # bcoz list is zero indexed
        
        '''Step 4 -> We will encounter this if no positives were found. This means that all the 
			         numbers are in the range [1....n]. So the missing positive number will be n+1'''
        
        return (n + 1)
"""