/*
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 &le; n &le; 1000
1 &le; m &le; min(50, n)

Examples: 

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.


*/
pub struct Solution {}
impl Solution {
    pub fn split_array(nums: Vec<i32>, m: i32) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::split_array(0));
  println!("Pass test cases!");
}
