# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        level = 0
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse the current level if it is an odd level
            if level % 2 == 1:
                current_level.reverse()
            
            result.append(current_level)
            level += 1
        
        return result

# Example usage
solution = Solution()

# Example 1
root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.zigzagLevelOrder(root1))  # Output: [[3], [20, 9], [15, 7]]

# Example 2
root2 = TreeNode(1)
print(solution.zigzagLevelOrder(root2))  # Output: [[1]]

# Example 3
root3 = None
print(solution.zigzagLevelOrder(root3))  # Output: []
