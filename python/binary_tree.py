class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class BinaryTree:
    def inorder(self, root):
        if not root: return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    
    def preorder(self, root):
        if not root: return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)
    
    def postorder(self, root):
        if not root: return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.val]
    
    def bfs(self, root):
        if not root: return []
        result, queue = [], [root]
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return result
    
    def max_depth(self, root):
        if not root: return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    bt = BinaryTree()
    print(bt.inorder(root))
