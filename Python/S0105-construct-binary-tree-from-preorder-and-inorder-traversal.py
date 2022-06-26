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
        def dfs(pstart,pend,istart,iend):
            if not (0<=pstart<=len(preorder) and pstart <= pend):
                return None
            
            r = TreeNode(preorder[pstart])
            for posi in range(istart,iend + 1):
                if r.val == inorder[posi]:
                    lsize = posi - istart
                    rsize = iend - posi
                    r.left = dfs(pstart + 1,pstart + lsize ,istart,posi - 1)
                    r.right = dfs(pend-rsize+1,pend,posi + 1,iend)
                    break
            return r

        r = dfs(0,len(preorder) - 1,0,len(preorder) - 1)
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
    preorder,inorder = [1,2,4,7,3,5,6],[2,7,4,1,5,3,6]
    assert vaildation(Solution().buildTree(preorder,inorder),preorder,inorder)
    
    preorder,inorder = [1,2,3],[2,3,1]
    assert vaildation(Solution().buildTree(preorder,inorder),preorder,inorder)

    preorder,inorder = [1,2],[1,2]
    assert vaildation(Solution().buildTree(preorder,inorder),preorder,inorder)

    preorder,inorder = [3,9,20,15,7],[9,3,15,20,7]
    assert vaildation(Solution().buildTree(preorder,inorder),preorder,inorder)

    preorder,inorder = [-1],[-1]
    assert vaildation(Solution().buildTree(preorder,inorder),preorder,inorder)
    