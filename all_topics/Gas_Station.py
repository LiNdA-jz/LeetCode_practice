class Solution:
    # 超出时间限制
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     n = len(gas)

    #     if n == 1:
    #         return 0 if gas[0] >= cost[0] else -1

    #     if sum(gas) < sum(cost):
    #         return -1

    #     diff = [0] * n

    #     for i in range(n):
    #         diff[i] = gas[i] - cost[i]
    #     # print(diff)

    #     i = 0
    #     cur_gas = 0

    #     while i < n:
    #         if cur_gas + diff[i] <= 0:
    #             i += 1
    #             cur_gas = 0
    #             continue
    #         for j in range(n):
    #             idx = (i + j) % n
    #             if diff[idx] == 0:
    #                 continue
    #             cur_gas += diff[idx]
    #             if cur_gas < 0:
    #                 break
    #         if cur_gas >= 0:
    #             return i
    #         else:
    #             cur_gas = 0
    #         i += 1

    #     return -1

    # 一次遍历
    # 通过减小被检查的加油站数目，来降低总的时间复杂度
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0

        while i < n:
            sum_of_gas = 0
            sum_of_cost = 0
            cnt = 0

            while cnt < n:
                j = (i + cnt) % n
                sum_of_gas += gas[j]
                sum_of_cost += cost[j]

                if sum_of_cost > sum_of_gas:
                    break
                cnt += 1

            if cnt == n:
                return i
            else:
                i = i + cnt + 1

        return -1