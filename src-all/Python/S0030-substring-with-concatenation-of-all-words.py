"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

 

Example 1:
Input:
  s = &quot;barfoothefoobarman&quot;,
  words = [&quot;foo&quot;,&quot;bar&quot;]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are &quot;barfoo&quot; and &quot;foobar&quot; respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input:
  s = &quot;wordgoodgoodgoodbestword&quot;,
  words = [&quot;word&quot;,&quot;good&quot;,&quot;best&quot;,&quot;word&quot;]
Output: []


"""
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        pass


if __name__ == '__main__':
    assert Solution().findSubstring(0) == 0

