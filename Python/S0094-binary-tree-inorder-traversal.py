"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        
        def inorder(n):
            if not n:
                return None
            
            inorder(n.left)
            lst.append(n.val)
            inorder(n.right)
            pass
        
        inorder(root)
        return lst


if __name__ == '__main__':
    assert Solution().inorderTraversal(0) == 0

