"""
Given n points in the plane that are all pairwise distinct, a &quot;boomerang&quot; is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

 

"""
from typing import List
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().numberOfBoomerangs(0) == 0

