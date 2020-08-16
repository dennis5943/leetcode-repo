"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.
 

Follow up:
Could you solve it using only O(1) extra space?
 

Example 1:
Input:
[&quot;a&quot;,&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;c&quot;,&quot;c&quot;,&quot;c&quot;]

Output:
Return 6, and the first 6 characters of the input array should be: [&quot;a&quot;,&quot;2&quot;,&quot;b&quot;,&quot;2&quot;,&quot;c&quot;,&quot;3&quot;]

Explanation:
&quot;aa&quot; is replaced by &quot;a2&quot;. &quot;bb&quot; is replaced by &quot;b2&quot;. &quot;ccc&quot; is replaced by &quot;c3&quot;.

 

Example 2:
Input:
[&quot;a&quot;]

Output:
Return 1, and the first 1 characters of the input array should be: [&quot;a&quot;]

Explanation:
Nothing is replaced.

 

Example 3:
Input:
[&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;]

Output:
Return 4, and the first 4 characters of the input array should be: [&quot;a&quot;,&quot;b&quot;,&quot;1&quot;,&quot;2&quot;].

Explanation:
Since the character &quot;a&quot; does not repeat, it is not compressed. &quot;bbbbbbbbbbbb&quot; is replaced by &quot;b12&quot;.
Notice each digit has it&#39;s own entry in the array.

 

Note:
	All characters have an ASCII value in [35, 126].
	1 <= len(chars) <= 1000.


"""
from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().compress(0) == 0

