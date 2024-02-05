"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    # not work
    # def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    #     if not node:
    #         return []
    #     elif not node.neighbors:
    #         return [Node(node.val)]

    #     node_new = []
    #     searched = [1]

    #     # print(len(node.neighbors))
    #     def cloned(cur_val, cur_node):
    #         if not node.neighbors:
    #             node_new.append(Node(node.val))
    #             return

    #         for i in cur_node.neighbors:
    #             if i.val in searched:
    #                 print(i.val, " searched")
    #                 if not cur_node.neighbors:
    #                     cur_node.neighbors = [Node(i.val)]
    #                 else:
    #                     cur_node.neighbors.append(Node(i.val))
    #                 # node_new.append(Node(cur_val, Node(i.val)))
    #                 continue
    #             print(i.val)
    #             node_new.append(Node(cur_val, [Node(i.val)]))
    #             searched.append(cur_val)
    #             cloned(i.val, i)

    #         return

    #     cloned(1, node)
    #     return node_new

    # 深度优先搜索
    # 用一种数据结构记录已经被克隆过的节点
    # 使用一个哈希表存储所有已被访问和克隆的节点。哈希表中的 key 是原始图中的节点，value 是克隆图中的对应节点。
    # 从给定节点开始遍历图。如果某个节点已经被访问过，则返回其克隆图中的对应节点。
    # 如果当前访问的节点不在哈希表中，则创建它的克隆节点并存储在哈希表中。
    # 递归调用每个节点的邻接点。每个节点递归调用的次数等于邻接点的数量
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node

        # 如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回
        if node in self.visited:
            return self.visited[node]

        # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
        clone_node = Node(node.val, [])

        # 哈希表存储
        self.visited[node] = clone_node

        # 遍历该节点的邻居并更新克隆节点的邻居列表
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/clone-graph/solutions/370663/ke-long-tu-by-leetcode-solution/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 广度优先遍历
    # 借助哈希表记录被克隆过的节点来避免陷入死循环
    # 将题目给定的节点添加到队列。克隆该节点并存储到哈希表中
    # 每次从队列首部取出一个节点，遍历该节点的所有邻接点。如果某个邻接点已被访问，则该邻接点一定在 visited 中，那么从 visited 获得该邻接点，否则创建一个新的节点存储在 visited 中，并将邻接点添加到队列。
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node

        visited = {}

        # 将题目给定的节点添加到队列
        queue = deque([node])
        # 克隆第一个节点并存储到哈希表中
        visited[node] = Node(node.val, [])

        # 广度优先搜索
        while queue:
            # 取出队列的头节点
            n = queue.popleft()
            # 遍历该节点的邻居
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # 如果没有被访问过，就克隆并存储在哈希表中
                    visited[neighbor] = Node(neighbor.val, [])
                    # 将邻居节点加入队列中
                    queue.append(neighbor)
                # 更新当前节点的邻居列表
                visited[n].neighbors.append(visited[neighbor])

        return visited[node]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/clone-graph/solutions/370663/ke-long-tu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。