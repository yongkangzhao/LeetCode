'''
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
'''
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
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
