"""
Created on Sun Nov 26 21:52:06 2017

@author: KangziLi
@source: lintcode - 73. Construct Binary Tree from Preorder and Inorder Traversal
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    Given preorder and inorder traversal of a tree, construct the binary tree.
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        tree = TreeNode(preorder[0])
        treeposi = inorder.index(preorder[0])
        tree.left = self.buildTree(preorder[1 : 1 + treeposi], inorder[: treeposi])
        tree.right = self.buildTree(preorder[1 + treeposi : ], inorder[treeposi+1:])
        return tree