# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # res = TreeNode()
        # res.val = root1.val + root2.val

        # def bfs(tree1, tree2):
        #     left, right = 0, 0
        #     if (tree1.left and tree2.left):
        #         left = tree1.left + tree2.left
        #     elif (tree1.left and not tree2.left):
        #         left = tree1.left
        #     elif (not tree1.left and tree2.left):
        #         left = tree2.left
        #     elif (not tree1.left and not tree2.left):
        #         left = None
        #     elif (tree1.right and tree2.right):
        #         right = tree1.right + tree2.right
        #     elif (tree1.right and not tree2.right):
        #         right = tree1.right
        #     elif (not tree1.right and tree2.right):
        #         right = tree2.right
        #     else:
        #         right = None

        #     return left, right

        # tree1, tree2 = root1, root2
        # while (tree1.left or tree1.right or tree2.left or tree2.right):
        #     left, right = bfs(tree1, tree2)
        #     res.left = left
        #     res.right = right
        #     tree1.val = 

        if not root1 and not root2: return None
        ans = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
        # None if not root1 else root1.left
        ans.left = self.mergeTrees(root1 and root1.left, root2 and root2.left)
        ans.right = self.mergeTrees(root1 and root1.right, root2 and root2.right)
        return ans

        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        else:
            return root1 or root2

        # bfs (deque)
        if not (root1 and root2):
            return root1 or root2
        queue1, queue2 = collections.deque([root1]), collections.deque([root2])
        while queue1 and queue2:
            node1, node2 = queue1.popleft(), queue2.popleft()
            if node1 and node2:
                node1.val = node1.val + node2.val
                if (not node1.left) and node2.left:
                    node1.left = TreeNode(0)
                if (not node1.right) and node2.right:
                    node1.right = TreeNode(0)
                queue1.append(node1.left)
                queue1.append(node1.right)
                queue2.append(node2.left)
                queue2.append(node2.right)
        return root1

# recursion
# Time complexity : O(m). A total of mm nodes need to be traversed. Here, m represents the minimum number of nodes from the two given trees.
# Space complexity : O(m). The depth of the recursion tree can go upto m in the case of a skewed tree. In average case, depth will be O(logm)


# /**
# * Definition for a binary tree node.
# * public class TreeNode {
# *     int val;
# *     TreeNode left;
# *     TreeNode right;
# *     TreeNode(int x) { val = x; }
# * }
# */
# public class Solution {
#     public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
#         if (t1 == null)
#             return t2;
#         if (t2 == null)
#             return t1;
#         t1.val += t2.val;
#         t1.left = mergeTrees(t1.left, t2.left);
#         t1.right = mergeTrees(t1.right, t2.right);
#         return t1;
#     }
# }

# iterative
# Time complexity : O(n). We traverse over a total of nn nodes. Here, n refers to the smaller of the number of nodes in the two trees.
# Space complexity : O(n). The depth of stack can grow upto n in case of a skewed tree.
#/**
#  * Definition for a binary tree node.
#  * public class TreeNode {
#  *     int val;
#  *     TreeNode left;
#  *     TreeNode right;
#  *     TreeNode(int x) { val = x; }
#  * }
#  */
# public class Solution {
#     public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
#         if (t1 == null)
#             return t2;
#         Stack < TreeNode[] > stack = new Stack < > ();
#         stack.push(new TreeNode[] {t1, t2});
#         while (!stack.isEmpty()) {
#             TreeNode[] t = stack.pop();
#             if (t[0] == null || t[1] == null) {
#                 continue;
#             }
#             t[0].val += t[1].val;
#             if (t[0].left == null) {
#                 t[0].left = t[1].left;
#             } else {
#                 stack.push(new TreeNode[] {t[0].left, t[1].left});
#             }
#             if (t[0].right == null) {
#                 t[0].right = t[1].right;
#             } else {
#                 stack.push(new TreeNode[] {t[0].right, t[1].right});
#             }
#         }
#         return t1;
#     }
# }

