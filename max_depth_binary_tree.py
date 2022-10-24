class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # def __init__(self):
    #     self.max_depth = 0

    def print_tree(self, node):
        print(node.val)
        if node.left:
            self.print_tree(node.left)
            self.print_tree(node.right)

    # with global
    # def get_max_depth(self, node, depth):
    #     if not node:
    #         return
    #
    #     depth += 1
    #     if depth > self.max_depth:
    #         self.max_depth = depth
    #
    #     self.get_max_depth(node.left, depth)
    #     self.get_max_depth(node.right, depth)

    # no global
    def get_max_depth(self, node: TreeNode, depth: int) -> int:
        if not node:
            return 0

        return 1 + max(self.get_max_depth(node.left, depth), self.get_max_depth(node.right, depth))


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
s = Solution()
print(s.get_max_depth(root, 0))
# print(s.max_depth)
