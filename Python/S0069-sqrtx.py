"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.


"""
class Solution:
    def mySqrt(self, x: int) -> int:
        #binary search the value n that n **2 <= x and x < (n+1)**2
        def binSearch(l:int, r:int):
            mid = int( (r + l) / 2 )
            if mid ** 2 <= x and (mid +1)**2 > x:
                return mid

            if mid ** 2 >= x:
                return binSearch(l,mid)
            else:
                return binSearch(mid + 1,r)
        
        return int(binSearch(0,x))


if __name__ == '__main__':
    assert Solution().mySqrt(26) == 5
    assert Solution().mySqrt(15) == 3
    assert Solution().mySqrt(8) == 2
    

