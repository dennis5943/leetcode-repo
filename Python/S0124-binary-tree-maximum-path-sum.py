"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def dfs(root):

            if not root:
                return 0 , 0 , 0
            
            l1,l2,l3 = dfs(root.left)
            r1,r2,r3 = dfs(root.right)
            a1,a2,a3 = max(l1,r1,root.val,r3,l3),root.val + max(l2,r2), l2 + root.val + r2
            return a1,a2,a3
        
        res = dfs(root)
        return max(res)

from pickle import LIST
def lst2tree(list: LIST) -> TreeNode:
    if not list:
        return None
    r = TreeNode(val = list[0])

    def dfs(node,idx):
        leftIdx = (idx + 1) * 2 - 1
        rightIdx = (idx + 1) * 2

        if leftIdx < len(list) and list[leftIdx]:
            node.left = TreeNode(val = list[leftIdx])
            dfs(node.left,leftIdx)
        
        if rightIdx < len(list) and list[rightIdx]:
            node.right = TreeNode(val = list[rightIdx])
            dfs(node.right,rightIdx)
    dfs(r,0)
    return r

if __name__ == '__main__':
    #assert Solution().maxPathSum(lst2tree([-3])) == -3
    assert Solution().maxPathSum(lst2tree([-10,9,20,None,None,15,7])) == 42
    assert Solution().maxPathSum(lst2tree([1,2,3])) == 6

