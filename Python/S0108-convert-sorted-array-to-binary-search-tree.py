"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def solve(left, right):
            if left > right: return None
            m = (left + right)//2
            return TreeNode(nums[m], solve(left,m-1), solve(m+1,right))
        return solve(0, len(nums)-1)

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

def validation(root:TreeNode) -> bool:
    def dfs(node):
        if not node:
            return True,0
        lres,lh = dfs(node.left)
        if not lres:
            return False,lh
        
        rres,rh = dfs(node.right)
        if not rres:
            return False,rh
        return abs(lh - rh) <= 1,1 + max(lh,rh)
    return dfs(root)[0]

if __name__ == '__main__':
    assert validation(Solution().sortedArrayToBST([-10,-3,0,5,9]))
    assert validation(Solution().sortedArrayToBST([1,3]))

