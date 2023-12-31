# 100. Same Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if (not p or not q) or (p.val != q.val):
        return False
    
    return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))

p, q = TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2))
print(isSameTree(p, q)) # False