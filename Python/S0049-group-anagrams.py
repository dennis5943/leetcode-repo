"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
	All inputs will be in lowercase.
	The order of your output does not matter.


"""
from typing import List
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictu = {}
        for i in strs:
            if ''.join(sorted(i)) not in dictu:
                dictu[''.join(sorted(i))] = [i]
            else:
                dictu[''.join(sorted(i))].append(i)
        return dictu.values()
      
if __name__ == '__main__':
    assert Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'],['tan', 'nat'],['bat']]
    assert Solution().groupAnagrams([""]) == [[""]]
    assert Solution().groupAnagrams(["a"]) == [["a"]]