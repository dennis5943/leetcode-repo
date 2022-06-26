"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dfs(node,pidx,iidx):
            if pidx == len(preorder):
                return None,pidx,iidx
            curNode = TreeNode(preorder[pidx])
            if not node:
                node = curNode

            if iidx < len(inorder) and preorder[pidx] == inorder[iidx]:
                node.right,pidx,iidx = dfs(curNode,pidx + 1,iidx + 2)
            else:
                curNode.left,pidx,iidx = dfs(curNode,pidx + 1,iidx)

            return curNode,pidx,iidx

        r = dfs(None,0,0)[0]
        return r

def vaildation(root: TreeNode,preorder: List[int],inorder: List[int]) -> bool:

    treePreorder = []
    treeInorder = []

    def dfs(root):
        if not root:
            return True

        treePreorder.append(root.val)
        dfs(root.left)
        treeInorder.append(root.val)
        dfs(root.right)

    dfs(root)
    return treePreorder == preorder and treeInorder == inorder

if __name__ == '__main__':
    preorder,inorder = [1,2,3],[2,3,1]
    #assert vaildation(Solution().buildTree(preorder,inorder),preorder,inorder)

    preorder,inorder = [1,2],[1,2]
    assert vaildation(Solution().buildTree(preorder,inorder),preorder,inorder)

    preorder,inorder = [3,9,20,15,7],[9,3,15,20,7]
    assert vaildation(Solution().buildTree(preorder,inorder),preorder,inorder)

    preorder,inorder = [-1],[-1]
    assert vaildation(Solution().buildTree(preorder,inorder),preorder,inorder)
    