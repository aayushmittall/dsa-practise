# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        stack = [[root,1]]
        res=1
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(depth,res)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
        return res
      
# BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        q = deque([root])  
        levels=0
        while q:
            length=len(q)
            for i in range(length):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levels += 1
        return levels
      
 # Recursive DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))
