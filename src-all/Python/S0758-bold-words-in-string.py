"""
Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = [&quot;ab&quot;, &quot;bc&quot;] and S = &quot;aabcd&quot;, we should return &quot;a<b>abc</b>d&quot;. Note that returning &quot;a<b>a<b>b</b>c</b>d&quot; would use more tags, so it is incorrect.

Constraints:
	words has length in range [0, 50].
	words[i] has length in range [1, 10].
	S has length in range [0, 500].
	All characters in words[i] and S are lowercase letters.

Note: This question is the same as 616: https://leetcode.com/problems/add-bold-tag-in-string/

"""
from typing import List
class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().boldWords(0) == 0

