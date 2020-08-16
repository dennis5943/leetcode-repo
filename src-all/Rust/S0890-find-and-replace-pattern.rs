/*
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

Example 1:
Input: words = [&quot;abc&quot;,&quot;deq&quot;,&quot;mee&quot;,&quot;aqq&quot;,&quot;dkd&quot;,&quot;ccc&quot;], pattern = &quot;abb&quot;
Output: [&quot;mee&quot;,&quot;aqq&quot;]
Explanation: &quot;mee&quot; matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
&quot;ccc&quot; does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.

 

Note:
	1 <= words.length <= 50
	1 <= pattern.length = words[i].length <= 20


*/
pub struct Solution {}
impl Solution {
    pub fn find_and_replace_pattern(words: Vec<String>, pattern: String) -> Vec<String> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::find_and_replace_pattern(0));
  println!("Pass test cases!");
}
