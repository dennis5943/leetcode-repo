"""
Given a string s, we make queries on substrings of s.

For each query queries[i] = [left, right, k], we may rearrange the substring s[left], ..., s[right], and then choose up to k of them to replace with any lowercase English letter. 

If the substring is possible to be a palindrome string after the operations above, the result of the query is true. Otherwise, the result is false.

Return an array answer[], where answer[i] is the result of the i-th query queries[i].

Note that: Each letter is counted individually for replacement so if for example s[left..right] = &quot;aaa&quot;, and k = 2, we can only replace two of the letters.  (Also, note that the initial string s is never modified by any query.)

 
Example :

Input: s = &quot;abcda&quot;, queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
Output: [true,false,false,true,true]
Explanation:
queries[0] : substring = &quot;d&quot;, is palidrome.
queries[1] : substring = &quot;bc&quot;, is not palidrome.
queries[2] : substring = &quot;abcd&quot;, is not palidrome after replacing only 1 character.
queries[3] : substring = &quot;abcd&quot;, could be changed to &quot;abba&quot; which is palidrome. Also this can be changed to &quot;baab&quot; first rearrange it &quot;bacd&quot; then replace &quot;cd&quot; with &quot;ab&quot;.
queries[4] : substring = &quot;abcda&quot;, could be changed to &quot;abcba&quot; which is palidrome.

 
Constraints:
	1 <= s.length, queries.length <= 10^5
	0 <= queries[i][0] <= queries[i][1] < s.length
	0 <= queries[i][2] <= s.length
	s only contains lowercase English letters.


"""
from typing import List
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        
        pass


if __name__ == '__main__':
    assert Solution().canMakePaliQueries(0) == 0

