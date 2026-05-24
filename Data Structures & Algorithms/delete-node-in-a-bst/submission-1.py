# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(root):
            while root.left != None:
                root = root.left
            return root

        if root == None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left == None and root.right == None:
                root = None
                return root
            elif root.left == None and root.right:
                root = root.right
                return root
            elif root.left and root.right == None:
                root = root.left
                return root
            else:
                tmp = findMin(root.right)
                root.val = tmp.val
                root.right = self.deleteNode(root.right, tmp.val)
        return root
