/*
A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k. There can be multiple ways to restore the array.

Return the number of possible array that can be printed as a string s using the mentioned program.

The number of ways could be very large so return it modulo 10^9 + 7

 
Example 1:
Input: s = &quot;1000&quot;, k = 10000
Output: 1
Explanation: The only possible array is [1000]

Example 2:
Input: s = &quot;1000&quot;, k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.

Example 3:
Input: s = &quot;1317&quot;, k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]

Example 4:
Input: s = &quot;2020&quot;, k = 30
Output: 1
Explanation: The only possible array is [20,20]. [2020] is invalid because 2020 > 30. [2,020] is ivalid because 020 contains leading zeros.

Example 5:
Input: s = &quot;1234567890&quot;, k = 90
Output: 34

 
Constraints:
	1 <= s.length <= 10^5.
	s consists of only digits and doesn&#39;t contain leading zeros.
	1 <= k <= 10^9.

*/
pub struct Solution {}
impl Solution {
    pub fn number_of_arrays(s: String, k: i32) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::number_of_arrays(0));
  println!("Pass test cases!");
}
