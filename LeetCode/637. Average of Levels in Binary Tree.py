# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 16:43:09 2018

@author: Kangzi Li

LeetCode: 637. Average of Levels in Binary Tree
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
      
        
class Solution(object): 
    def dfs(self,root,ans,depth):
        if not root:
            return 
        if depth == len(ans):
            ans.append([root.val,1.0])
        else:
            ans[depth][0]+=root.val
            ans[depth][1]+=1
        self.dfs(root.left,ans,depth+1)
        self.dfs(root.right,ans,depth+1)
        
    
    
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # BFS
        avg = []
        if not root:
            return avg
        queue = [root]
        while queue:
            total,cnt = 0,len(queue)
            for i in range(cnt):
                node = queue.pop(0)
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avg.append(float(total)/cnt)
        return 
        #DFS
#        ans = []
#        if not root:
#            return ans
#        self.dfs(root,ans,0)
#        return [a[0]/a[1] for a in ans]
    
    
    