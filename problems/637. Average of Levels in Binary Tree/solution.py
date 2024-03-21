"""
Runtime
44
ms

Beats
62.20%
of users with Python3

Memory
18.47
MB

Beats
59.48%
of users with Python3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def update(self, node, step):
        self.step_val_dict[step].append(node.val)
        if node.left:
            self.update(node.left, step+1)
        if node.right:
            self.update(node.right, step+1)

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.step_val_dict = defaultdict(list)
        self.update(root, 0)

        result = []
        for _, values in self.step_val_dict.items():
            result.append(sum(values)/len(values))
        return result