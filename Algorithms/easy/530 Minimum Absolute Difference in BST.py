'''
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 

Note:

There are at least two nodes in this BST.
This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
'''
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.minimum = inf
        self.dfs(root)
        return self.minimum

    def dfs(self, node):
        left       = self.dfs(node.left) if node.left else None
        right      = self.dfs(node.right) if node.right else None
        left_diff  = node.val - left[1] if left else inf
        right_diff = right[0] - node.val if right else inf
        abs_diff = min(left_diff , right_diff)
        self.minimum = min(self.minimum, abs_diff)
        return [min(left[0] if left else inf,right[0] if right else inf,node.val), max(right[1] if right else -inf,left[1] if left else -inf,node.val)]
