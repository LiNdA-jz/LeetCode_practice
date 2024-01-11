# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        if root.left == None and root.right == None:
            return [[root.val]]

        node_dict = {}

        level, pre_level = 0, []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                pre_level.append(level)
                if level in node_dict.keys():
                    node_dict[level].append(root.val)
                else:
                    node_dict[level] = [root.val]
                root = root.left
                level += 1

            root = stack.pop()
            root = root.right
            level = pre_level.pop() + 1

        print(node_dict)
        res = []
        for val in node_dict.values():
            res.append(val)

        return res

    # 广度优先搜索
    # 用一个二元组 (node, level) 来表示状态
    # 首先根元素入队
    # 当队列不为空的时候
    # 求当前队列的长度 si
    # 依次从队列中取 si 个元素进行拓展，然后进入下一次迭代
    # 普通广度优先搜索每次只取一个元素拓展，而这里每次取 si 个元素
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []

        if root == None:
            return ret

        q = []
        q.append(root)

        while q:
            current_level_size = len(q)
            ret.append([])

            for i in range(current_level_size):
                # popleft!!!
                node = q.pop(0)
                ret[-1].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ret