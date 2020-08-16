/*
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:

	The hundreds digit represents the depth D of this node, 1 <= D <= 4.
	The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
	The units digit represents the value V of this node, 0 <= V <= 9.

Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5, you need to return the sum of all paths from the root towards the leaves.

It&#39;s guaranteed that the given list represents a valid connected binary tree.

Example 1:
Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.

 

Example 2:
Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
    3
     \
      1

The path sum is (3 + 1) = 4.


*/
pub struct Solution {}
impl Solution {
    pub fn path_sum(nums: Vec<i32>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::path_sum(0));
  println!("Pass test cases!");
}
