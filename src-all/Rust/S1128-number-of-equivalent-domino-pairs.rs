/*
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 
Example 1:
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

 
Constraints:
	1 <= dominoes.length <= 40000
	1 <= dominoes[i][j] <= 9

*/
pub struct Solution {}
impl Solution {
    pub fn num_equiv_domino_pairs(dominoes: Vec<Vec<i32>>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::num_equiv_domino_pairs(0));
  println!("Pass test cases!");
}
