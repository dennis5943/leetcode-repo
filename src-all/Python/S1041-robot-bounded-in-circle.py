"""
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

	&quot;G&quot;: go straight 1 unit;
	&quot;L&quot;: turn 90 degrees to the left;
	&quot;R&quot;: turn 90 degress to the right.

The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:
Input: &quot;GGLLGG&quot;
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:
Input: &quot;GG&quot;
Output: false
Explanation: 
The robot moves north indefinitely.

Example 3:
Input: &quot;GL&quot;
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

 

Note:
	1 <= instructions.length <= 100
	instructions[i] is in {&#39;G&#39;, &#39;L&#39;, &#39;R&#39;}


"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().isRobotBounded(0) == 0

