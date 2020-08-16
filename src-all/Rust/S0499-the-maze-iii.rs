/*
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), but it won&#39;t stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

Given the ball position, the hole position and the maze, find out how the ball could drop into the hole by moving the shortest distance. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the hole (included). Output the moving directions by using &#39;u&#39;, &#39;d&#39;, &#39;l&#39; and &#39;r&#39;. Since there could be several different shortest ways, you should output the lexicographically smallest way. If the ball cannot reach the hole, output &quot;impossible&quot;.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.

 

Example 1:
Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (0, 1)

Output: &quot;lul&quot;

Explanation: There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by &quot;lul&quot;.
The second way is up -> left, represented by &#39;ul&#39;.
Both ways have shortest distance 6, but the first way is lexicographically smaller because &#39;l&#39; < &#39;u&#39;. So the output is &quot;lul&quot;.

Example 2:
Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (3, 0)

Output: &quot;impossible&quot;

Explanation: The ball cannot reach the hole.

 

Note:
	There is only one ball and one hole in the maze.
	Both the ball and hole exist on an empty space, and they will not be at the same position initially.
	The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
	The maze contains at least 2 empty spaces, and the width and the height of the maze won&#39;t exceed 30.


*/
pub struct Solution {}
impl Solution {
    pub fn find_shortest_way(maze: Vec<Vec<i32>>, ball: Vec<i32>, hole: Vec<i32>) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::find_shortest_way(0));
  println!("Pass test cases!");
}
