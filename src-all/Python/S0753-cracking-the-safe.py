"""
There is a box protected by a password. The password is a sequence of n digits where each digit can be one of the first k digits 0, 1, ..., k-1.

While entering a password, the last n digits entered will automatically be matched against the correct password.

For example, assuming the correct password is &quot;345&quot;, if you type &quot;012345&quot;, the box will open because the correct password matches the suffix of the entered password.

Return any password of minimum length that is guaranteed to open the box at some point of entering it.

 

Example 1:
Input: n = 1, k = 2
Output: &quot;01&quot;
Note: &quot;10&quot; will be accepted too.

Example 2:
Input: n = 2, k = 2
Output: &quot;00110&quot;
Note: &quot;01100&quot;, &quot;10011&quot;, &quot;11001&quot; will be accepted too.

 

Note:
	n will be in the range [1, 4].
	k will be in the range [1, 10].
	k^n will be at most 4096.

 

"""
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().crackSafe(0) == 0

