"""
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, &quot;great acting skills&quot; and &quot;fine drama talent&quot; are similar, if the similar word pairs are pairs = [[&quot;great&quot;, &quot;fine&quot;], [&quot;acting&quot;,&quot;drama&quot;], [&quot;skills&quot;,&quot;talent&quot;]].

Note that the similarity relation is not transitive. For example, if &quot;great&quot; and &quot;fine&quot; are similar, and &quot;fine&quot; and &quot;good&quot; are similar, &quot;great&quot; and &quot;good&quot; are not necessarily similar.

However, similarity is symmetric. For example, &quot;great&quot; and &quot;fine&quot; being similar is the same as &quot;fine&quot; and &quot;great&quot; being similar.

Also, a word is always similar with itself. For example, the sentences words1 = [&quot;great&quot;], words2 = [&quot;great&quot;], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = [&quot;great&quot;] can never be similar to words2 = [&quot;doubleplus&quot;,&quot;good&quot;].

Note:
	The length of words1 and words2 will not exceed 1000.
	The length of pairs will not exceed 2000.
	The length of each pairs[i] will be 2.
	The length of each words[i] and pairs[i][j] will be in the range [1, 20].

 

"""
from typing import List
class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().areSentencesSimilar(0) == 0

