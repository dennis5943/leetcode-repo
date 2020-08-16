"""
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = [&quot;abcdef&quot;,&quot;uvwxyz&quot;] and deletion indices {0, 2, 3}, then the final array after deletions is [&quot;bef&quot;, &quot;vyz&quot;], and the remaining columns of A are [&quot;b&quot;,&quot;v&quot;], [&quot;e&quot;,&quot;y&quot;], and [&quot;f&quot;,&quot;z&quot;].  (Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]]).

Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.

Return the minimum possible value of D.length.

 
Example 1:
Input: A = [&quot;cba&quot;,&quot;daf&quot;,&quot;ghi&quot;]
Output: 1
Explanation: 
After choosing D = {1}, each column [&quot;c&quot;,&quot;d&quot;,&quot;g&quot;] and [&quot;a&quot;,&quot;f&quot;,&quot;i&quot;] are in non-decreasing sorted order.
If we chose D = {}, then a column [&quot;b&quot;,&quot;a&quot;,&quot;h&quot;] would not be in non-decreasing sorted order.

Example 2:
Input: A = [&quot;a&quot;,&quot;b&quot;]
Output: 0
Explanation: D = {}

Example 3:
Input: A = [&quot;zyx&quot;,&quot;wvu&quot;,&quot;tsr&quot;]
Output: 3
Explanation: D = {0, 1, 2}

 
Constraints:
	1 <= A.length <= 100
	1 <= A[i].length <= 1000


"""
from typing import List
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().minDeletionSize(0) == 0

