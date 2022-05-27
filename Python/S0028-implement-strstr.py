"""
Implement strStr().
Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string?
This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

Constraints:
	haystack and needle consist only of lowercase English characters.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
            
        needleLen = len(needle)
        haystackLen = len(haystack)

        for i in range(haystackLen):
            if haystack[i] == needle[0] and (i + needleLen - 1) < haystackLen and haystack[i + needleLen - 1] == needle[-1]:
                substr = haystack[i:i + needleLen]
                if substr == needle:
                    return i

        return -1

if __name__ == '__main__':
    assert Solution().strStr("hello", "ll") == 2
    assert Solution().strStr("hello", "lo") == 3
    assert Solution().strStr("hello", "lop") == -1
    assert Solution().strStr("aaaaa", "bba") == -1
    assert Solution().strStr("aaaaa", "") == 0
    assert Solution().strStr("abxabcabcaby", "abcaby") ==  6
