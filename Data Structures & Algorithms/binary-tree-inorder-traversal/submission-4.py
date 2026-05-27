class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        l = []
        l.extend(self.inorderTraversal(root.left))
        l.append(root.val)
        l.extend(self.inorderTraversal(root.right))
        return l