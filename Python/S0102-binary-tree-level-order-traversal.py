"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]


"""
from pickle import LIST
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []

        def dfs(node,lv):
            if node:
                if lv == len(ans):
                    ans.append([])
                ans[lv].append(node.val)
                dfs(node.left,lv +1)
                dfs(node.right,lv +1)

            pass
        dfs(root,0)
        return ans

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
    assert Solution().levelOrder(lst2tree([3,9,20,None,None,15,7])) == [[3],[9,20],[15,7]]
    assert Solution().levelOrder(lst2tree([1])) == [[1]]
    assert Solution().levelOrder(lst2tree([])) == []

