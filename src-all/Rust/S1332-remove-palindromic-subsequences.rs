/*
Given a string s consisting only of letters &#39;a&#39; and &#39;b&#39;. In a single step you can remove one palindromic subsequence from s.

Return the minimum number of steps to make the given string empty.

A string is a subsequence of a given string, if it is generated by deleting some characters of a given string without changing its order.

A string is called palindrome if is one that reads the same backward as well as forward.

 
Example 1:
Input: s = &quot;ababa&quot;
Output: 1
Explanation: String is already palindrome

Example 2:
Input: s = &quot;abb&quot;
Output: 2
Explanation: &quot;abb&quot; -> &quot;bb&quot; -> &quot;&quot;. 
Remove palindromic subsequence &quot;a&quot; then &quot;bb&quot;.

Example 3:
Input: s = &quot;baabb&quot;
Output: 2
Explanation: &quot;baabb&quot; -> &quot;b&quot; -> &quot;&quot;. 
Remove palindromic subsequence &quot;baab&quot; then &quot;b&quot;.

Example 4:
Input: s = &quot;&quot;
Output: 0

 
Constraints:
	0 <= s.length <= 1000
	s only consists of letters &#39;a&#39; and &#39;b&#39;

*/
pub struct Solution {}
impl Solution {
    pub fn remove_palindrome_sub(s: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::remove_palindrome_sub(0));
  println!("Pass test cases!");
}
