class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def print_tree(self, node):
        print(node.val)
        if node.left:
            self.print_tree(node.left)
            self.print_tree(node.right)

    def invert_tree(self, node) -> TreeNode:
        """
        :type node: TreeNode
        :rtype: TreeNode
        """
        if not node:
            return None

        left = node.left
        node.left = node.right
        node.right = left
        self.invert_tree(node.left)
        self.invert_tree(node.right)


s = Solution()
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
s.print_tree(root)
s.invert_tree(root)
s.print_tree(root)
