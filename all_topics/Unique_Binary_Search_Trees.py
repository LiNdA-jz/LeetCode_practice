class Solution:
    def numTrees(self, n: int) -> int:
        num_dict = {}
        if n == 1:
            num_dict[n] = 1
            return 1

        tree_num = 0

        for i in range(1, n + 1):
            left = i - 1
            right =  n - i

            if left == 0:
                if right in num_dict.keys():
                    tree_num += num_dict[right]
                else:
                    num_dict[right] = self.numTrees(right)
                    tree_num += num_dict[right]
            elif right == 0:
                if left in num_dict.keys():
                    tree_num += num_dict[left]
                else:
                    num_dict[left] = self.numTrees(left)
                    tree_num += num_dict[left]

            else:
                if left in num_dict.keys() and right in num_dict.keys():
                    tree_num += num_dict[left] * num_dict[right]
                elif left in num_dict.keys():
                    num_dict[right] = self.numTrees(right)
                    tree_num += num_dict[left] * num_dict[right]
                elif right in num_dict.keys():
                    num_dict[left] = self.numTrees(left)
                    tree_num += num_dict[left] * num_dict[right]
                else:
                    num_dict[right] = self.numTrees(right)
                    num_dict[left] = self.numTrees(left)
                    tree_num += num_dict[right] * num_dict[left]

        # print(num_dict)

        return tree_num

    # 动态规划
    # 将 1⋯(i−1) 序列作为左子树，将 (i+1)⋯n 序列作为右子树
    # 原问题可以分解成规模较小的两个子问题，且子问题的解可以复用。因此，我们可以想到使用动态规划来求解本题。
    # G(n): 长度为 n 的序列能构成的不同二叉搜索树的个数
    # F(i,n): 以 i 为根、序列长度为 n 的不同二叉搜索树个数
    # G(n) 可以从 F(i,n) 得到
    # F(i,n) 又会递归地依赖于 G(n)
    # G(n)= ∑_{i = 1}^{n} F(i,n)
    # 举例而言，创建以 3 为根、长度为 7 的不同二叉搜索树，整个序列是 [1,2,3,4,5,6,7]，我们需要从左子序列 [1,2] 构建左子树，从右子序列 [4,5,6,7] 构建右子树，然后将它们组合（即笛卡尔积）
        # F(3,7)
        # 将 [1,2] 构建不同左子树的数量表示为 G(2)
        # [4,5,6,7] 构建不同右子树的数量表示为 G(4)
        # F(3,7)=G(2)⋅G(4) -> F(i,n)=G(i−1)⋅G(n−i) -> G(n)= ∑_{i = 1}^{n} G(i−1)⋅G(n−i)

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/unique-binary-search-trees/solutions/329807/bu-tong-de-er-cha-sou-suo-shu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


    # 数学
    # G(n)函数的值在数学上被称为卡塔兰数 Cn
    # C0 = 1,C{n+1} = 2(2n + 1) / (n + 2) * Cn
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2 * (2 * i + 1) / (i + 2)
        return int(C)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/unique-binary-search-trees/solutions/329807/bu-tong-de-er-cha-sou-suo-shu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。