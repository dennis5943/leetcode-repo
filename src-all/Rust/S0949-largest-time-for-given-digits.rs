/*
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:
Input: [1,2,3,4]
Output: &quot;23:41&quot;

Example 2:
Input: [5,5,5,5]
Output: &quot;&quot;

 

Note:
	A.length == 4
	0 <= A[i] <= 9


*/
pub struct Solution {}
impl Solution {
    pub fn largest_time_from_digits(a: Vec<i32>) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::largest_time_from_digits(0));
  println!("Pass test cases!");
}
