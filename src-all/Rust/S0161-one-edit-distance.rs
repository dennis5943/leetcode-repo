/*
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

	Insert a character into s to get t
	Delete a character from s to get t
	Replace a character of s to get t

Example 1:
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert &#39;c&#39; into s to get t.

Example 2:
Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.

Example 3:
Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace &#39;0&#39; with &#39;1&#39; to get t.

*/
pub struct Solution {}
impl Solution {
    pub fn is_one_edit_distance(s: String, t: String) -> bool {
        
    }
}

fn main() {
  assert_eq!(0, Solution::is_one_edit_distance(0));
  println!("Pass test cases!");
}
