"""
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

	Insert a character into s to get t
	Delete a character from s to get t
	Replace a character of s to get t

Example 1:
Input: s = &quot;ab&quot;, t = &quot;acb&quot;
Output: true
Explanation: We can insert &#39;c&#39; into s to get t.

Example 2:
Input: s = &quot;cab&quot;, t = &quot;ad&quot;
Output: false
Explanation: We cannot get t from s by only one step.

Example 3:
Input: s = &quot;1203&quot;, t = &quot;1213&quot;
Output: true
Explanation: We can replace &#39;0&#39; with &#39;1&#39; to get t.

"""
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().isOneEditDistance(0) == 0

