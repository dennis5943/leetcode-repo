"""
You want to form a target string of lowercase letters.

At the beginning, your sequence is target.length &#39;?&#39; marks.  You also have a stamp of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to 10 * target.length turns.

For example, if the initial sequence is &quot;?????&quot;, and your stamp is &quot;abc&quot;,  then you may make &quot;abc??&quot;, &quot;?abc?&quot;, &quot;??abc&quot; in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is &quot;ababc&quot;, and the stamp is &quot;abc&quot;, then we could return the answer [0, 2], corresponding to the moves &quot;?????&quot; -> &quot;abc??&quot; -> &quot;ababc&quot;.

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.  Any answers specifying more than this number of moves will not be accepted.

 

Example 1:
Input: stamp = &quot;abc&quot;, target = &quot;ababc&quot;
Output: [0,2]
([1,0,2] would also be accepted as an answer, as well as some other answers.)

Example 2:
Input: stamp = &quot;abca&quot;, target = &quot;aabcaca&quot;
Output: [3,0,1]

 

Note:
	1 <= stamp.length <= target.length <= 1000
	stamp and target only contain lowercase letters.

"""
from typing import List
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        pass


if __name__ == '__main__':
    assert Solution().movesToStamp(0) == 0

