class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums_set = set(nums)

        for i in nums_set:
            if nums.count(i) == 1:
                return i

    # 哈希表
    # 使用哈希映射统计数组中每个元素的出现次数
    def singleNumber(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        ans = [num for num, occ in freq.items() if occ == 1][0]
        return ans

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/single-number-ii/solutions/746993/zhi-chu-xian-yi-ci-de-shu-zi-ii-by-leetc-23t6/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 依次确定每一个二进制位
    # 依次计算答案的每一个二进制位是 0 还是 1
    # 考虑答案的第 i 个二进制位, 对于数组中非答案的元素，每一个元素都出现了 3 次，对应着第 i 个二进制位的 3 个 0 或 3 个 1
    # -> 它们的和都是 3 的倍数（即和为 0 或 3
    # -> 答案的第 i 个二进制位就是数组中所有元素的第 i 个二进制位之和除以 3 的余数
    # 对于数组中的每一个元素 x, 使用位运算 (x >> i) & 1 得到 x 的第 i 个二进制位, 并将它们相加再对 3 取余, 得到的结果一定为 0 或 1
    # 在某些语言（例如 Python）中需要对最高位进行特殊判断 ->
    # 「有符号整数类型」（即 int类型）的第 31 个二进制位（即最高位）是补码意义下的符号位，对应着 -2^{31}，而「无符号整数类型」由于没有符号，第 31 个二进制位对应着 2^{31}
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/single-number-ii/solutions/746993/zhi-chu-xian-yi-ci-de-shu-zi-ii-by-leetc-23t6/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 数字电路设计
    # 四种门电路
    # 非门
    # 与门
    # 或门
    # 异或门: A⊕B
    # 使用一个「黑盒」存储当前遍历过的所有整数, 「黑盒」的第 i 位为 {0,1,2} 三者之一, 表示当前遍历过的所有整数的第 i 位之和除以 3 的余数
    # a 的第 i 位为 0 且 b 的第 i 位为 0，表示 0
    # a 的第 i 位为 0 且 b 的第 i 位为 1，表示 1
    # a 的第 i 位为 1 且 b 的第 i 位为 0，表示 2
    # 当我们遍历到一个新的整数 x 时，对于 x 的第 i 位 xi ，如果 xi=0，那么 a 和 b 的第 i 位不变
    # 如果 xi=1，那么 a 和 b 的第 i 位按照 (00)→(01)→(10)→(00) 这一循环进行变化
    # 转换为等价的整数位运算
    # a = (~a & b & x) | (a & ~b & ~x)
    # b = ~a & (bˆx)
    # 当我们遍历完数组中的所有元素后，(ai, bi) 要么是 (00)，表示答案的第 i 位是 0；要么是 (01)，表示答案的第 i 位是 1。因此我们只需要返回 b 作为答案即可
    # ai 和 bi 是「同时」得出结果的
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            a, b = (~a & b & num) | (a & ~b & ~num), ~a & (b ^ num)
        return b

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/single-number-ii/solutions/746993/zhi-chu-xian-yi-ci-de-shu-zi-ii-by-leetc-23t6/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 数字电路设计优化
    # 方法三中计算 b 的规则较为简单，而 a 的规则较为麻烦 -> 将「同时计算」改为「分别计算」，即先计算出 b，再拿新的 b 值计算 a
    # b = ~a & (b ˆ x)
    # a = ~b & (a ˆ x)

    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for num in nums:
            b = ~a & (b ^ num)
            a = ~b & (a ^ num)
        return b

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/single-number-ii/solutions/746993/zhi-chu-xian-yi-ci-de-shu-zi-ii-by-leetc-23t6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。