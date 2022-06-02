"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        boundP = ["r","d","l","u"]
        idx = 0

        while any( 1 for r in matrix for c in r):
            if boundP[idx] == "r":
                res.extend(matrix[0])
                del matrix[0]
            elif boundP[idx] == "d":
                for r in matrix:
                    res.append(r[-1])
                    del r[-1]
            elif boundP[idx] == "l":
                matrix[-1].reverse()
                res.extend(matrix[-1])
                del matrix[-1]
            elif boundP[idx] == "u":
                for ridx in range(len(matrix)-1,-1,-1):
                    res.append(matrix[ridx][0])
                    del matrix[ridx][0]
            idx = (idx + 1)%4
        return res

if __name__ == '__main__':
    assert Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]) == [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
    assert Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    assert Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]

