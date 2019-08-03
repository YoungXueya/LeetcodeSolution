# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # BFS
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue=collections.deque()
        if root:
            queue.append(root)
        while queue:
            node=queue.pop()
            temp=node.left
            node.left=node.right
            node.right=temp
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
            
            
    
    # DFS
    def invertTree2(self, root: TreeNode) -> TreeNode:
        stack=[]
        if root:
            stack.append(root)
        while stack:
            node=stack.pop()
            temp=node.left
            node.left=node.right
            node.right=temp
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
            
    def invertTree1(self, root: TreeNode) -> TreeNode:
        if root:
            return self.invert(root)
        else:
            return None
    
    def invert(self,root):
        temp=None
        if root.left:
            root.left=self.invert(root.left)
        if root.right:
            root.right=self.invert(root.right)
        temp=root.right
        root.right=root.left
        root.left=temp
        return root
