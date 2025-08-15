from typing import List


class Solution:
    # [7, 1, 5, 3, 6, 4]
    def maxProfit(self, prices: List[int]) -> int:
        # 0 1 2 3 4 5
        # [7 1 5 3 6 4]
        # x o o x o x
        # 遍历顺序 从左到右，
        # [1, 5], [1, 3], [1, 6], [1, 4] 可能的组合
        # 状态是profit?
        # Input:   7 1 5
        # Profile: 0 0
        # Since it's a combination of two numbers, so dp should be a 2D array
        # [cost][price]
        # [ 7 - 7, 1 - 7, 5 - 7, 3 - 7, 6 - 7, 4  - 7,]
        # [     0, 1 - 1, 5 - 1, 3 - 1, 6 - 1, 4 - 1,]
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]
        #

        # [1, 5]
        # [1][2]
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 4, 0, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]

        # [1, 3]
        # [1][3]
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 4, 2, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]

        # [1, 3]
        #
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]
        # [ 0, 0, 0, 0, 0, 0,]

        # 如果我这样构造dp状态，并不是每个格子都有数据，
        # 而且两个状态之间，也没有递推的关系
        #
        #
        # 0 1 2 3 4 5
        # [7 1 5 3 6 4]

        # 最低 7: 0, 0, 0,      0, 0, 0
        # 最低 i = 1  1: 0, 0, 4, 2 -> 4, 5, 5 max(j - 1, prices[j] - prices[i])
        # 最低 i = 2  5: 0, 0, 0,      1, 1, 5 max(j - 1, prices[j] - prices[2])
        # 最低 i = 3  5: 0, 0, 0,      1, 1, 5 max(j - 1, prices[j] - prices[3])
        # 最低 i = 4  5: 0, 0, 0,      1, 1, 5 max(j - 1, prices[j] - prices[3])

        # 第1天买，最佳成本是7
        # 第2天买，最佳成本是1
        # 第3天买，最佳成本是1
        # 第4天买，最佳成本是1
        # 第5天买，最佳成本是1
        # 第6天买，最佳成本是1

        # 第1天卖，最佳出价是7
        # 第2天卖，最佳出价是1
        # 第3天卖，最佳出价是5
        # 第4天卖，最佳出价是1
        # 第5天卖，最佳出价是1
        # 第6天卖，最佳出价是1

        # min_cost = [7, 1, 1, 1, 1, 1]
        # min_cost[i] = min(min_cost[i - 1], prices[i])
        # max_profit[i] = max(max_profit[i - 1], price[i] - min_cost[i])

        #  0 1 2 3 4 5
        # [7 1 5 3 6 4]

        #    0   1   2   3   4   5 - price
        # 0 [_, -6, -2, -4, -1, -3]
        # 1 [_,  _,  4,  2,  5,  3]
        # 2 [_,  _,  _, -2,  1, -1]
        # 3 [_,  _,  _,  _,  3,  1]
        # 4 [_,  _,  _,  _,  _, -2]
        # 5 [_,  _,  _,  _,  _,  _]
        #
        # cost
        #
        # [7, 1]                  -> -6
        # [7, 1, 5]               ->  4
        # [7, 1, 5, 3]            ->  4
        # [7, 1, 5, 3, 6]         ->  5
        # [7, 1, 5, 3, 6, 4]      ->  5
        # 用这种方式不行，因为通过新加入的元素和之前子问题的profit，无法计算出新的profit
        # 要计算新的profit，需要的是子问题的最低cost。
        # [7]                     ->  7
        # [7, 8]                  ->  7
        # [7, 8, 5]               ->  5
        # [7, 8, 5, 3]            ->  3
        # [7, 8, 5, 3, 6]         ->  3
        # [7, 8, 5, 3, 6, 4]      ->  3
        # 所以每个子问题都需要有两个值，一个是最小成本，一个是最大利润
        #                             最小成本·最大利润
        # [7, 8]                  ->  7·-1
        # [7, 8, 5]               ->  5·-1
        # [7, 8, 5, 3]            ->  3·-1
        # [7, 8, 5, 3, 6]         ->  3·3
        # [7, 8, 5, 3, 6, 4]      ->  3·3
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]

        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

        return dp[n - 1][1]


def cheapest_buy_price(prices: List[int]) -> int:
    # [7]                     ->  7
    # [7, 8]                  ->  7
    # [7, 8, 5]               ->  5
    # [7, 8, 5, 3]            ->  3
    # [7, 8, 5, 3, 6]         ->  3
    # [7, 8, 5, 3, 6, 4]      ->  3
    # 这个题可以这样解决，是因为前面的子问题对应的状态是“最小值”，我们新的最小值只需要和之前的最小值比较。
    if not prices:
        return 0  # 或者抛异常，看需求
    n = len(prices)
    min_cost = [0] * n
    min_cost[0] = prices[0]
    for i in range(1, n):
        min_cost[i] = min(min_cost[i - 1], prices[i])
    return min_cost[-1]


def cheapest_buy_day(prices: List[int]) -> int:
    if not prices:
        return -1  # 无数据
    n = len(prices)
    min_day = [0] * n
    for i in range(1, n):
        if prices[i] < prices[min_day[i - 1]]:
            min_day[i] = i
        else:
            min_day[i] = min_day[i - 1]
    return min_day[-1]  # 返回的是索引，0-based


print(cheapest_buy_price([7, 2, 5, 3, 6, 4]))
print(cheapest_buy_day([7, 2, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 2, 5, 3, 6, 4]))
