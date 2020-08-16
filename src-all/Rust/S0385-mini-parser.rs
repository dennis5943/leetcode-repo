/*
Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

	String is non-empty.
	String does not contain white spaces.
	String contains only digits 0-9, [, - ,, ].

 

Example 1:
Given s = &quot;324&quot;,

You should return a NestedInteger object which contains a single integer 324.

 

Example 2:
Given s = &quot;[123,[456,[789]]]&quot;,

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.

 

*/
pub struct Solution {}
impl Solution {
    pub fn deserialize(s: String) -> NestedInteger {
        
    }
}

fn main() {
  assert_eq!(0, Solution::deserialize(0));
  println!("Pass test cases!");
}
