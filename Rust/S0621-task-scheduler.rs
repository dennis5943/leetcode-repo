/*
You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.

 
Example 1:
Input: tasks = [&quot;A&quot;,&quot;A&quot;,&quot;A&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = [&quot;A&quot;,&quot;A&quot;,&quot;A&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
[&quot;A&quot;,&quot;A&quot;,&quot;A&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;]
[&quot;A&quot;,&quot;B&quot;,&quot;A&quot;,&quot;B&quot;,&quot;A&quot;,&quot;B&quot;]
[&quot;B&quot;,&quot;B&quot;,&quot;B&quot;,&quot;A&quot;,&quot;A&quot;,&quot;A&quot;]
...
And so on.

Example 3:
Input: tasks = [&quot;A&quot;,&quot;A&quot;,&quot;A&quot;,&quot;A&quot;,&quot;A&quot;,&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;D&quot;,&quot;E&quot;,&quot;F&quot;,&quot;G&quot;], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

 
Constraints:
	The number of tasks is in the range [1, 10000].
	The integer n is in the range [0, 100].


*/
pub struct Solution {}
impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::least_interval(0));
  println!("Pass test cases!");
}
