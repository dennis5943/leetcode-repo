"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
	If there is no such window in S that covers all characters in T, return the empty string "".
	If there is such window, you are guaranteed that there will always be only one unique minimum window in S.


"""
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc = Counter(t)
        sc = Counter(s)
        for k in [kk for kk in sc.keys() if kk not in tc]:
            del sc[k]

        if any( 1 for k in tc.keys() if tc[k] > sc[k]):
            return ""

        l = 0
        r = len(s) - 1

        minStr = lambda s1,s2: s1 if len(s1) <= len(s2) else s2
        def dfs(ll,rr):
            while s[ll] not in tc:
                ll += 1

            while s[rr] not in tc:
                rr -= 1

            tstr = s[ll:rr + 1]
            llch = s[ll]
            rrch = s[rr]

            if sc[llch] > tc[llch]:
                sc[s[ll]] -= 1
                lshift = dfs(ll+1,rr)
                sc[s[ll]] += 1
                if lshift:
                    tstr = minStr(lshift,tstr)
            
            if sc[rrch] > tc[rrch]:
                sc[s[rr]] -= 1
                rshift = dfs(ll,rr - 1)
                sc[s[rr]] += 1
                if rshift:
                    tstr = minStr(rshift,tstr)    

            return tstr
        substr = dfs(l,r)
        return substr


if __name__ == '__main__':
    assert Solution().minWindow("wegdtzwabazduwwdysdetrrctotpcepalxdewzezbfewbabbseinxbqqplitpxtcwwhuyntbtzxwzyaufihclztckdwccpeyonumbpnuonsnnsjscrvpsqsftohvfnvtbphcgxyumqjzltspmphefzjypsvugqqjhzlnylhkdqmolggxvneaopadivzqnpzurmhpxqcaiqruwztroxtcnvhxqgndyozpcigzykbiaucyvwrjvknifufxducbkbsmlanllpunlyohwfsssiazeixhebipfcdqdrcqiwftutcrbxjthlulvttcvdtaiwqlnsdvqkrngvghupcbcwnaqiclnvnvtfihylcqwvderjllannflchdklqxidvbjdijrnbpkftbqgpttcagghkqucpcgmfrqqajdbynitrbzgwukyaqhmibpzfxmkoeaqnftnvegohfudbgbbyiqglhhqevcszdkokdbhjjvqqrvrxyvvgldtuljygmsircydhalrlgjeyfvxdstmfyhzjrxsfpcytabdcmwqvhuvmpssingpmnpvgmpletjzunewbamwiirwymqizwxlmojsbaehupiocnmenbcxjwujimthjtvvhenkettylcoppdveeycpuybekulvpgqzmgjrbdrmficwlxarxegrejvrejmvrfuenexojqdqyfmjeoacvjvzsrqycfuvmozzuypfpsvnzjxeazgvibubunzyuvugmvhguyojrlysvxwxxesfioiebidxdzfpumyon","ozgzyywxvtublcl") == "fsrvmrnczjzjevkdvroiluthhpqtff"
    assert Solution().minWindow("cgklivwehljxrdzpfdqsapogwvjtvbzahjnsejwnuhmomlfsrvmrnczjzjevkdvroiluthhpqtffhlzyglrvorgnalk","mqfff") == "fsrvmrnczjzjevkdvroiluthhpqtff"
    assert Solution().minWindow("ab","a") == "a"
    assert Solution().minWindow("JJDDDADOBECODEBANC","ABC") == "BANC"
    assert Solution().minWindow("a","a") == "a"
    assert Solution().minWindow("a","aa") == ""

