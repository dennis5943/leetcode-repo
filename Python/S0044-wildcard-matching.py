"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:
	s could be empty and contains only lowercase letters a-z.
	p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input:
s = "acdcb"
p = "a*c?b"
Output: false

1 2 3 4 5 6 7 8
3~6
range(3,)

"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def trymatch(pl, pr,sl,sr):
            if any(p) and pr >= pl and all('*'== p[i] for i in range(pl,pr + 1)):
                return True            
            elif pl > pr:
                return sl > sr
            elif sl > sr or s == '':
                return pl > pr

            tmpptn = p[pl:pr+1]
            ssl = s[sl]
            ssr = s[sr]
            if p[pl] in ['?', s[sl]]:
                return trymatch(pl + 1,pr,sl + 1,sr)
            elif p[pr] in ['?',s[sr]]:
                return trymatch(pl,pr - 1,sl, sr -1)
            elif p[pl] == '*' and p[pr] == '*':
                return trymatch(pl + 1,pr,sl + 1,sr) or trymatch(pl,pr-1,sl ,sr) \
                    or trymatch(pl + 1,pr,sl ,sr) or trymatch(pl,pr - 1,sl ,sr) \
                    or trymatch(pl,pr,sl + 1,sr) or trymatch(pl,pr,sl ,sr - 1)
            else:
                return False

        pleft = 0
        pright = len(p) - 1

        sleft = 0
        sright = len(s) - 1

        return trymatch(pleft,pright,sleft,sright)

if __name__ == '__main__':
    assert Solution().isMatch('babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab','***bba**a*bbba**aab**b') == True
    assert Solution().isMatch('','') == True
    assert Solution().isMatch('a','a*') == True
    assert Solution().isMatch('a','') == False
    assert Solution().isMatch('','a') == False
    assert Solution().isMatch('abcabczzzde','*abc???de*') == True
    assert Solution().isMatch('','******') == True
    assert Solution().isMatch('ab','?*') == True
    assert Solution().isMatch('aa','a') == False
    assert Solution().isMatch('aa','*') == True
    assert Solution().isMatch('cb','?a') == False
    assert Solution().isMatch('adceb','*a*b') == True
    assert Solution().isMatch('acdcb','a*c?b') == False

