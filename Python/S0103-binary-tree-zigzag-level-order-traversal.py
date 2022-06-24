"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
from pickle import LIST

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []

        def dfs(node,lv):
            if node:
                if lv == len(ans):
                    ans.append([])
                
                if lv%2 == 0:
                    ans[lv].append(node.val)
                else:
                    ans[lv] = [node.val] + ans[lv]
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
    assert Solution().zigzagLevelOrder(lst2tree([3,9,20,None,None,15,7])) == [[3],[20,9],[15,7]]

