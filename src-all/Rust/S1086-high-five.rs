/*
Given a list of scores of different students, return the average score of each student&#39;s top five scores in the order of each student&#39;s id.

Each entry items[i] has items[i][0] the student&#39;s id, and items[i][1] the student&#39;s score.  The average score is calculated using integer division.

 

Example 1:
Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.

 

Note:
	1 <= items.length <= 1000
	items[i].length == 2
	The IDs of the students is between 1 to 1000
	The score of the students is between 1 to 100
	For each student, there are at least 5 scores

*/
pub struct Solution {}
impl Solution {
    pub fn high_five(items: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::high_five(0));
  println!("Pass test cases!");
}
