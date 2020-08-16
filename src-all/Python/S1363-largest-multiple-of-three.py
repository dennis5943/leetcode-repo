"""
Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.

Since the answer may not fit in an integer data type, return the answer as a string.

If there is no answer return an empty string.

 
Example 1:
Input: digits = [8,1,9]
Output: &quot;981&quot;

Example 2:
Input: digits = [8,6,7,1,0]
Output: &quot;8760&quot;

Example 3:
Input: digits = [1]
Output: &quot;&quot;

Example 4:
Input: digits = [0,0,0,0,0,0]
Output: &quot;0&quot;

 
Constraints:
	1 <= digits.length <= 10^4
	0 <= digits[i] <= 9
	The returning answer must not contain unnecessary leading zeros.


"""
from typing import List
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().largestMultipleOfThree(0) == 0

