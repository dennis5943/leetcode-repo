#190. Reverse Bits
"""
Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

input:  43261596 (00000010100101000001111010011100)
output:964176192 (00111001011110000010100101000000)
                    111001011110000010100101
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        cnt = 0
        while n:
            t = n % 2
            n = n >>1
            ans = (ans << 1) + t
            cnt = cnt + 1
        
        for c in range(cnt,32):
            ans = ans << 1
        return ans


if __name__ == '__main__':
    #print(11,11>>1, 11%2)

    #print(5<<1) #101 => 1010
    print(Solution().reverseBits(43261596))
    #print(Solution().reverseBits(6)) #110=>011(3)