# 94. Binary Tree Inorder Traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode) -> list[int]:
    path = []
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        path.append(cur.val)
        cur = cur.right
    
    return path

root = TreeNode(1, None , TreeNode(2, TreeNode(3), None))
print(inorderTraversal(root)) # [1,3,2]