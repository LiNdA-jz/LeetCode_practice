# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        ret = []
        q = [root]

        asc = True

        while q:
            ret.append([])

            for _ in range(len(q)):
                cur = q.pop(0)

                if asc:
                    ret[-1].append(cur.val)
                else:
                    ret[-1] = [cur.val] + ret[-1]

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            asc = not asc

        return ret

    # 广度优先遍历
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if root == None:
            return ans

        nodeQueue = []
        nodeQueue.append(root)
        isOrderLeft = True

        while nodeQueue:
            levelList = []
            size = len(nodeQueue)

            for _ in range(size):
                node = nodeQueue.pop(0)

                if isOrderLeft:
                    levelList.append(node.val)
                else:
                    levelList = [node.val] + levelList

                if node.left:
                    nodeQueue.append(node.left)

                if node.right:
                    nodeQueue.append(node.right)

            ans.append(levelList)
            isOrderLeft = not isOrderLeft

        return ans