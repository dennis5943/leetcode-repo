"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:
Input: [&quot;bella&quot;,&quot;label&quot;,&quot;roller&quot;]
Output: [&quot;e&quot;,&quot;l&quot;,&quot;l&quot;]

Example 2:
Input: [&quot;cool&quot;,&quot;lock&quot;,&quot;cook&quot;]
Output: [&quot;c&quot;,&quot;o&quot;]

 

Note:
	1 <= A.length <= 100
	1 <= A[i].length <= 100
	A[i][j] is a lowercase letter


"""
from typing import List
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().commonChars(0) == 0

