# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        def inorder(root, l):
            if root.left != None:
                inorder(root.left, l)
            l.append(root.val)
            if root.right != None:
                inorder(root.right, l)
        l = []

        inorder(root, l)

        return l
        