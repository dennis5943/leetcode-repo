"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


"""
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        def dfs(lv,tgtlv):
            if lv == tgtlv:
                return
            elif lv < 2:
                res.append([1] * (lv + 1))            
            else:                
                nums = [1] + [res[lv-1][i] + res[lv-1][i + 1] for i in range(lv-1)] + [1]
                res.append(nums)

            dfs(lv + 1,numRows)

        dfs(0,numRows)
        return res

if __name__ == '__main__':
    assert Solution().generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    assert Solution().generate(1) == [[1]]

