/*
Given a binary string s (a string consisting only of &#39;0&#39; and &#39;1&#39;s).

Return the number of substrings with all characters 1&#39;s.

Since the answer may be too large, return it modulo 10^9 + 7.

 
Example 1:
Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1&#39;s characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.

Example 2:
Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.

Example 3:
Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1&#39;s characters.

Example 4:
Input: s = "000"
Output: 0

 
Constraints:
	s[i] == &#39;0&#39; or s[i] == &#39;1&#39;
	1 <= s.length <= 10^5

*/
pub struct Solution {}
impl Solution {
    pub fn num_sub(s: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::num_sub(0));
  println!("Pass test cases!");
}
