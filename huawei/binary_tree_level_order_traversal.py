# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # not work for [3,9,20,null,null,15,7]
        # expect: [[3],[9,20],[15,7]]; got: [[3],[9,20],[[15],[7]]] -> extra bracket
        # if root == None:
        #     return []

        # if (root.left == None) and (root.right == None):
        #     return [[root.val]]

        # elif (root.left == None):
        #     return [self.levelOrder(root.right)]
        # elif (root.right == None):
        #     return [self.levelOrder(root.left)]
        # else:
        #     return [[root.val]] + [[root.left.val, root.right.val]] + [self.levelOrder(root.left.left) + self.levelOrder(root.left.right) + self.levelOrder(root.right.left) + self.levelOrder(root.right.right)]

        if root == None:
            return [] # 特判

        # use deque
        # >>> from collections import deque
        # >>> deq = deque([1, 2, 3])
        # >>> deq.appendleft(5)
        # >>> deq.append(6)
        # >>> deq
        # deque([5, 1, 2, 3, 6])
        # >>> deq.popleft()
        # 5
        # >>> deq.pop()
        # 6
        # >>> deq
        # deque([1, 2, 3])
        q = collections.deque([root]) # 双端队列
        ans = []
        while len(q) != 0:
            q_len = len(q)
            cur_vals = []
            for _ in range(q_len): # 遍历当前层节点
                cur = q.popleft() # 从左边弹出队列
                cur_vals.append(cur.val) # 将当前节点值加入当前层的列表
                if cur.left != None:
                    q.append(cur.left)
                if cur.right != None:
                    q.append(cur.right)
            ans.append(cur_vals) # 将当前层结果加入答案列表
        return ans