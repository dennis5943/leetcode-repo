/*
You are given a string s containing lowercase letters and an integer k. You need to :

	First, change some characters of s to other lowercase English letters.
	Then divide s into k non-empty disjoint substrings such that each substring is palindrome.

Return the minimal number of characters that you need to change to divide the string.

 
Example 1:
Input: s = "abc", k = 2
Output: 1
Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.

Example 2:
Input: s = "aabbc", k = 3
Output: 0
Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.

Example 3:
Input: s = "leetcode", k = 8
Output: 0

 
Constraints:
	1 <= k <= s.length <= 100.
	s only contains lowercase English letters.

*/
pub struct Solution {}
impl Solution {
    pub fn palindrome_partition(s: String, k: i32) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::palindrome_partition(0));
  println!("Pass test cases!");
}
