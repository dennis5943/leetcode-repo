/*
With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:

	word contains the first letter of puzzle.
	For each letter in word, that letter is in puzzle.
	For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage"; while invalid words are "beefed" (doesn&#39;t include "a") and "based" (includes "s" which isn&#39;t in the puzzle).

Return an array answer, where answer[i] is the number of words in the given word list words that are valid with respect to the puzzle puzzles[i].
 
Example :

Input: 
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation:
1 valid word for "aboveyz" : "aaaa" 
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There&#39;re no valid words for "gaswxyz" cause none of the words in the list contains letter &#39;g&#39;.

 
Constraints:
	1 <= words.length <= 10^5
	4 <= words[i].length <= 50
	1 <= puzzles.length <= 10^4
	puzzles[i].length == 7
	words[i][j], puzzles[i][j] are English lowercase letters.
	Each puzzles[i] doesn&#39;t contain repeated characters.


*/
pub struct Solution {}
impl Solution {
    pub fn find_num_of_valid_words(words: Vec<String>, puzzles: Vec<String>) -> Vec<i32> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::find_num_of_valid_words(0));
  println!("Pass test cases!");
}
