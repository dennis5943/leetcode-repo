/*
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.

If there&#39;re duplicates in arr, count them seperately.

 
Example 1:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Example 2:
Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there&#39;s no 2, 4, 6, or 8 in arr.

Example 3:
Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

Example 4:
Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted cause 2 is in arr.

Example 5:
Input: arr = [1,1,2]
Output: 2
Explanation: Both 1s are counted because 2 is in the array.

 
Constraints:
	1 <= arr.length <= 1000
	0 <= arr[i] <= 1000

*/
pub struct Solution {}
impl Solution {
    pub fn count_elements(arr: Vec<i32>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::count_elements(0));
  println!("Pass test cases!");
}
