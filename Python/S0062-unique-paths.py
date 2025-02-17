"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Above is a 7 x 3 grid. How many possible unique paths are there?

 
Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28

 
Constraints:
	1 <= m, n <= 100
	It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.


"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #(m - 1 + n - 1)! / (m -1)!* (n-1)! = (m -1 + n - 1)* ....m / (n-1)!  
        if m < n :
            m,n = n,m

        res = 1
        for mm in range(m+n-2,m-1,-1):
            res *= mm
        
        for mm in range(1, n):
            res /= mm
        return int(res)


if __name__ == '__main__':
    assert Solution().uniquePaths(3,7) == 28
    assert Solution().uniquePaths(3,2) == 3

