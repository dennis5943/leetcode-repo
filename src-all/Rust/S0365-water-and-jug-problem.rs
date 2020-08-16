/*
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

	Fill any of the jugs completely with water.
	Empty any of the jugs.
	Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.

Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True

Example 2:
Input: x = 2, y = 6, z = 5
Output: False

 
Constraints:
	0 <= x <= 10^6
	0 <= y <= 10^6
	0 <= z <= 10^6


*/
pub struct Solution {}
impl Solution {
    pub fn can_measure_water(x: i32, y: i32, z: i32) -> bool {
        
    }
}

fn main() {
  assert_eq!(0, Solution::can_measure_water(0));
  println!("Pass test cases!");
}
