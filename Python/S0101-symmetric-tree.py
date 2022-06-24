"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

 

Follow up: Solve it both recursively and iteratively.

"""
from pickle import LIST
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def CheckSame(left,right):
            if left and right:
                return CheckSame(left.left,right.right) and CheckSame(left.right,right.left) if left.val == right.val else False
            return not left and not right

        return CheckSame(root.left,root.right) if root else False        

def lst2tree(list: LIST) -> TreeNode:

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
    assert Solution().isSymmetric(lst2tree([1,2,2,3,4,4,3])) == True
    assert Solution().isSymmetric(lst2tree([1,2,2,None,3,None,3])) == False

