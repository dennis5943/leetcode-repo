"""
Given n, how many structurally unique BST&#39;s (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST&#39;s:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

 
Constraints:
	1 <= n <= 19


"""
class Solution:
    def numTrees(self, n: int) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().numTrees(0) == 0

