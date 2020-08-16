/*
There&#39;s a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. Your goal is to find the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one. The squirrel can only take at most one nut at one time and can move in four directions - up, down, left and right, to the adjacent cell. The distance is represented by the number of moves.
Example 1:
Input: 
Height : 5
Width : 7
Tree position : [2,2]
Squirrel : [4,4]
Nuts : [[3,0], [2,5]]
Output: 12
Explanation:
<U+200B><U+200B><U+200B><U+200B><U+200B>

Note:
	All given positions won&#39;t overlap.
	The squirrel can take at most one nut at one time.
	The given positions of nuts have no order.
	Height and width are positive integers. 3 <= height * width <= 10,000.
	The given positions contain at least one nut, only one tree and one squirrel.


*/
pub struct Solution {}
impl Solution {
    pub fn min_distance(height: i32, width: i32, tree: Vec<i32>, squirrel: Vec<i32>, nuts: Vec<Vec<i32>>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::min_distance(0));
  println!("Pass test cases!");
}
