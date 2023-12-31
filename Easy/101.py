# 101. Symmetric Tree
class  TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    def dfs(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
    
    return dfs(root.left, root.right)

root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(isSymmetric(root)) # True

