"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

"""
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n= len(height)
        ptrl= 0
        ptrr= n-1
        water= 0
        maxLeft= height[ptrl]
        maxRight= height[ptrr]
        
        while ptrl < ptrr:
            
            if height[ptrl]<= height[ptrr]:
                ptrl+=1
                maxLeft= max(maxLeft, height[ptrl])
                water+= (maxLeft- height[ptrl])
            else:
                ptrr-=1
                maxRight= max(maxRight, height[ptrr])
                water+= (maxRight- height[ptrr])
        return water


if __name__ == '__main__':
    assert Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert Solution().trap([4,2,0,3,2,5]) == 9

