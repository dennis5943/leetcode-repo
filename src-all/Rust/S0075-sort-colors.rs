/*
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library&#39;s sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
	A rather straight forward solution is a two-pass algorithm using counting sort.
	First, iterate the array counting number of 0&#39;s, 1&#39;s, and 2&#39;s, then overwrite array with total number of 0&#39;s, then 1&#39;s and followed by 2&#39;s.
	Could you come up with a one-pass algorithm using only constant space?


*/
pub struct Solution {}
impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        
    }
}

fn main() {
  assert_eq!(0, Solution::sort_colors(0));
  println!("Pass test cases!");
}
