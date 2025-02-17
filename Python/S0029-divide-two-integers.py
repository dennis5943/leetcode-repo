"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Note:
	Both dividend and divisor will be 32-bit signed integers.
	The divisor will never be 0.
	Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [&minus;231,  231 &minus; 1]. For the purpose of this problem, assume that your function returns 231 &minus; 1 when the division result overflows.


"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend * divisor < 0:
            ans = int((abs(dividend) - abs(dividend) % abs(divisor)) / abs(divisor) * -1)
        else:
            ans = int((abs(dividend) - abs(dividend) % abs(divisor)) / abs(divisor))

        ans = max(ans, (-2)**31)
        ans = min(ans, (2)**31 -1)
        return ans

if __name__ == '__main__':

    assert Solution().divide(-2147483648,-1) == 2147483647
    assert Solution().divide(10,3) == 3
    assert Solution().divide(7,-3) == -2

