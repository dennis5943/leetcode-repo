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

        plist = list(filter(lambda x:any(x), p.split("*")))

        def valid(ptn,sstart):
            #if sstart + len(ptn) -1 > send:
            #    return False
            if sstart + len(ptn) -1 <= send:
                return all(ptn[i] in [s[i + sstart],'?'] for i in range(len(ptn)))
            else:
                return False

        sstart = 0
        send = len(s) - 1
        if all(pp == '*' for pp in p):
            return True if any(p) else s == ''

        if p[0] != '*':
            if valid(plist[0],0):
                sstart = len(plist[0])
                del plist[0]
            else:
                return False                
        if p[-1] != '*':
            if not any(plist):
                return sstart > send
            elif any(plist) and valid(plist[-1], max(sstart,len(s) - len(plist[-1]))):
                send -= len(plist[-1])
                del plist[-1]
            else:
                return False
        
        while any(plist):
            ptn = plist[0]
            del plist[0]
            isValid = False
            for i in range(sstart,send +1):
                remainStr = s[sstart:send + 1]
                if valid(ptn,i):
                    isValid = True
                    sstart = i + len(ptn)
                    break
            
            if not isValid:
                return False

        return True

if __name__ == '__main__':
    #assert Solution().isMatch('bbbbab','*a?*b') == False
    assert Solution().isMatch('c','*?*') == True
    assert Solution().isMatch('b','?*?') == False
    assert Solution().isMatch('mississippi','m??*ss*?i*pi') == False
    assert Solution().isMatch('babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab','***bba**a*bbba**aab**b') == False
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

