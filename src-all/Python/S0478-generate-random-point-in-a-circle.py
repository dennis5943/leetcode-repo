"""
Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Note:
	input and output values are in floating-point.
	radius and x-y position of the center of the circle is passed into the class constructor.
	a point on the circumference of the circle is considered to be in the circle.
	randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.

Example 1:
Input: 
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

Example 2:
Input: 
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution&#39;s constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if there aren&#39;t any.


"""

class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

from typing import List
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        

    def randPoint(self) -> List[float]:
        


# param_1 = obj.randPoint()
        pass


if __name__ == '__main__':
    assert Solution().__init__(0) == 0

