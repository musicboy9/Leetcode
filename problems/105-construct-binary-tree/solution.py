"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description
Runtime
42
ms

Beats
98.54%
of users with Python3

Memory
18.08
MB

Beats
92.24%
of users with Python3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec_tree(self, p_start, p_end, i_start, i_end):
        if p_start == p_end:
            return None
        root = self.preorder[p_start]
        if (p_end-p_start) == 1:
            return TreeNode(val=root)
        
        root_inorder_index = self.inorder_index_by_value[root]
        left_len = root_inorder_index - i_start

        return TreeNode(
            val=root,
            left=self.rec_tree(
                p_start=p_start+1,
                p_end=p_start+1+left_len,
                i_start=i_start,
                i_end=i_start+left_len
            ),
            right=self.rec_tree(
                p_start=p_start+1+left_len,
                p_end=p_end,
                i_start=i_start+left_len+1,
                i_end=i_end
            )
        )


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder

        self.preorder_index_by_value = {}
        self.inorder_index_by_value = {}
        for i in range(len(preorder)):
            self.preorder_index_by_value[preorder[i]] = i
            self.inorder_index_by_value[inorder[i]] = i
        
        return self.rec_tree(
            p_start=0,
            p_end=len(preorder),
            i_start=0,
            i_end=len(inorder)
        )
        
