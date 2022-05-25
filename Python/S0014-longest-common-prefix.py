"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.

"""
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        prefix = ""
        minlen = min(len(str) for str in strs)
        for i in range(minlen):
            if any(str for str in strs if strs[0][i] != str[i]):
                break
            else:
                prefix = prefix + strs[0][i]
            


        return prefix

if __name__ == '__main__':
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix(["flower", "flowery", "flow"]) == "flow"
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert Solution().longestCommonPrefix(["carerr", "car"]) == "car"
    assert Solution().longestCommonPrefix([]) == ""

