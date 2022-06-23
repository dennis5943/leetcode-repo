"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

"""
class Solution:
    def numDecodings(self, s: str) -> int:
        lst = [int(c) for c in s]

        if lst[0] == 0:
            return 0

        tmp = {}
        def dfs(p,i):
            v = p * 10 + lst[i] if p!=-1 else lst[i]
            
            if "{}_{}".format(p,i) in tmp:
                return tmp["{}_{}".format(p,i)]
            elif i < len(lst) -1:
                if p in [1,2] and (1<=v<=26):
                    tmp["{}_{}".format(p,i)] = dfs(-1,i+1)
                    return tmp["{}_{}".format(p,i)]
                elif p == -1 and (1<=v<=26):
                    tmp["{}_{}".format(p,i)] = dfs(lst[i],i+1) + dfs(-1,i+1)      
                    return tmp["{}_{}".format(p,i)]
                else:
                    tmp["{}_{}".format(p,i)] = 0
                    return 0
            elif i == len(lst) - 1 and (1<=v<=26):
                tmp["{}_{}".format(p,i)] = 1
                return 1
            else:
                tmp["{}_{}".format(p,i)] = 0
                return 0
        return dfs(-1,0)


if __name__ == '__main__':
    assert Solution().numDecodings("2839") == 1
    assert Solution().numDecodings("111111111111111111111111111111111111111111111") == 1836311903
    assert Solution().numDecodings('2101') == 1
    assert Solution().numDecodings('10') == 1
    assert Solution().numDecodings('06') == 0
    assert Solution().numDecodings('226') == 3
    assert Solution().numDecodings('12') == 2

