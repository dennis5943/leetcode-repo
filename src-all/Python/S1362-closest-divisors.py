"""
Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.

 
Example 1:
Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 &amp; 3, for num + 2 = 10, the closest divisors are 2 &amp; 5, hence 3 &amp; 3 is chosen.

Example 2:
Input: num = 123
Output: [5,25]

Example 3:
Input: num = 999
Output: [40,25]

 
Constraints:
	1 <= num <= 10^9


"""
from typing import List
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        
        pass


if __name__ == '__main__':
    assert Solution().closestDivisors(0) == 0

