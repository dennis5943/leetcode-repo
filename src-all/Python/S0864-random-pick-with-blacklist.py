"""
Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system&rsquo;s Math.random().

Note:
	1 <= N <= 1000000000
	0 <= B.length < min(100000, N)
	[0, N) does NOT include N. See interval notation.

Example 1:
Input: 
[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
[[1,[]],[],[],[]]
Output: [null,0,0,0]

Example 2:
Input: 
[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
[[2,[]],[],[],[]]
Output: [null,1,1,1]

Example 3:
Input: 
[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]

Example 4:
Input: 
[&quot;Solution&quot;,&quot;pick&quot;,&quot;pick&quot;,&quot;pick&quot;]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution&#39;s constructor has two arguments, N and the blacklist B. pick has no arguments. Arguments are always wrapped with a list, even if there aren&#39;t any.

"""
from typing import List
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        

    def pick(self) -> int:
        


# param_1 = obj.pick()
        pass


if __name__ == '__main__':
    assert Solution().__init__(0) == 0

