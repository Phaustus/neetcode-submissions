class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def travel(node):
            if node is None:
                return 0
            
            left_height = travel(node.left)
            if left_height == -1:
                return -1
            
            right_height = travel(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
                
            return max(left_height, right_height) + 1

        return travel(root) != -1