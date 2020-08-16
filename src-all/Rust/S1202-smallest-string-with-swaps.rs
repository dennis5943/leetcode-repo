/*
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

 
Example 1:
Input: s = &quot;dcab&quot;, pairs = [[0,3],[1,2]]
Output: &quot;bacd&quot;
Explaination: 
Swap s[0] and s[3], s = &quot;bcad&quot;
Swap s[1] and s[2], s = &quot;bacd&quot;

Example 2:
Input: s = &quot;dcab&quot;, pairs = [[0,3],[1,2],[0,2]]
Output: &quot;abcd&quot;
Explaination: 
Swap s[0] and s[3], s = &quot;bcad&quot;
Swap s[0] and s[2], s = &quot;acbd&quot;
Swap s[1] and s[2], s = &quot;abcd&quot;

Example 3:
Input: s = &quot;cba&quot;, pairs = [[0,1],[1,2]]
Output: &quot;abc&quot;
Explaination: 
Swap s[0] and s[1], s = &quot;bca&quot;
Swap s[1] and s[2], s = &quot;bac&quot;
Swap s[0] and s[1], s = &quot;abc&quot;

 
Constraints:
	1 <= s.length <= 10^5
	0 <= pairs.length <= 10^5
	0 <= pairs[i][0], pairs[i][1] < s.length
	s only contains lower case English letters.


*/
pub struct Solution {}
impl Solution {
    pub fn smallest_string_with_swaps(s: String, pairs: Vec<Vec<i32>>) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::smallest_string_with_swaps(0));
  println!("Pass test cases!");
}
