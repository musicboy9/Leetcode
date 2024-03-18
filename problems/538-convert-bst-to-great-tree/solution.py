"""
https://leetcode.com/problems/convert-bst-to-greater-tree/description/
Runtime
43
ms

Beats
99.32%
of users with Python3

Memory
18.49
MB

Beats
89.45%
of users with Python3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec_add_nodes(self, root):
        if not root:
            return []
        self.rec_add_nodes(root.right)
        self.nodes.append(root)
        self.rec_add_nodes(root.left)


    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.nodes = []
        self.rec_add_nodes(root)
        
        temp_sum = 0
        for n in self.nodes:
            val = n.val
            n.val += temp_sum
            temp_sum += val
        
        return root