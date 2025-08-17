from typing import List


class Solution:
    def maxProfit(self, prices):
        hold = -float('inf')
        sold = 0
        for p in prices:
            hold = max(hold, sold - p)
            sold = max(sold, hold + p)
        return sold
        # [7, 1, 5, 3, 6, 4]    min  profit
        #  7,                    7     0
        #  7, 1,                 1     0
        #  7, 1, 5,              5     4           4 = 5 - 1
        #  7, 1, 5, 3,           3     0           4 = 5 - 1
        #  7, 1, 5, 3, 6,        3     3           7 = 5 - 1 + 6 - 3
        #  7, 1, 5, 3, 6, 4,     6     0           7 = 5 - 1 + 6 - 3

        # [7, 1, 5, 3, 6, 4]    min
        #  7,
        #  7, 1,
        #  7, 1, 5,              1      4
        #  7, 1, 5, 3,           1      2          min(1, 3)
        #  7, 1, 5, 3, 6,
        #  7, 1, 5, 6, 3, 6, 4,
        # 我觉得这题没有办法再用min_cost来状态转移了
        # 因为后续状态不仅仅是依据min_cost来做决策的
        # 连续上升到最高点的时候卖
        # 跌下去的时候买 7
        # 所以需要当前值和前面的最后一个值和买的价格
        # [7, 1, 1, 1, 3, 3, 4,] costs[i] = min(costs[i - 1], price)
        # [7, 0, 0, 6, 0, 6, 0,] if sell[i - 1] > sell[i]: sell[i - 1]  = price[i - 1]
        # [0, 0, 0, 5, 5, 8, 8,] profits[i] = profits[i - 1] + sell[i] - cost[i]

        n = len(prices)
        costs = [float('inf')] * (n + 1)
        profits = [0] * (n + 1)


# Solution().maxProfit([7, 1, 5, 6, 3, 8, 4])
# [7, 1, 5, 6, 3, 8, 4]
# [7, 1, 5] -> 4 = 5 - 1      price - min_cost
# [7, 1, 5, 6] -> 5 = 6 - 1
# [7, 1, 5, 6, 3] -> 4 = 5 - 1
# [7, 1, 5, 6, 3, 8] -> 9 = 4 + ( 8 - 3 )

# [7, 1, 5] 		-> 4 = 5 - 1
# [7, 1, 5, 6] 		-> 5 = 6 - 1
# [7, 1, 5, 6, 2] 	-> 5
# [7, 1, 5, 6, 2, 7]  -> 10 = 5 + ( 7 - 2 )

# 针对[7, 1, 5, 6, 3, 8, 4]，有没有其他状态我不知道，一定有一个profits[i]的状态，内容是[0, 0, 4, 5, 5, 10, 10]✅
# [7, 1, 5, 6, 3, 8, 4]
# [0, 0, 4, 5, 5, 10, 10]

# i = 3
# profits[i - 1]: 4, prices[i]: 6, lowest_costs[i - 1]: 1
# -> profits[i] = profits[i - 1] + max(prices[i - 1] - prices[i - 1], 0)

def calculate(books: List[int]):
    n = len(books)
    counts = [float('inf')] * (n + 1)
    for i, book in enumerate(books):
        if book < counts[i]:
            counts[i + 1] = book
        else:
            counts[i + 1] = counts[i]
    print(counts)
    #
    #   i 0  1  2  3  4  5  6
    #    [7, 1, 5, 6, 3, 6, 4]
    # [_, 7, 1, 1, 1, 1, 1, 1]


calculate([4, 6, 8, 2, 4, 12])

# books = [4,6,8,2,4,12]
# 表示第0个书架上4本书
# 第一个书架6本书
# 从这些书架里面的一个书架里拿走所有书，其他书架拿一半的书，用dp来计算最多一共拿走多少本？
# [4] -> 4
# [4, 6] -> 2 + 6
from typing import List

from typing import List


def find_books(books: List[int]) -> int:
    n = len(books)

    dp = [[0] * (n + 1)] * (n + 1)
    count = [0] * (n + 1)
    for length in range(1, n + 1):  # 1 ~ n
        for l in range(n + 1 - length):
            r = l + length
            best = 0
            for m in range(l, r):
                best = max(best, dp[l][m] + dp[m][r] + books[m])
            dp[l][r] = best

    return dp[0][n]


find_books([4, 6, 8, 2, 4, 12])

# [  4, 6, 8, 2, 4, 12,  ]
# [inf, 4, 4, 4, 2,  2, 2]

# [4, 6, 8, 2, 4, 1]
#
# [0, 4,,, , ]
# [0, 0, 6,,, ]
# [0, 0, 0, 8,,]
# [0, 0, 0, 0, 2, ]
# [0, 0, 0, 0, 0, 4, ]
# [0, 0, 0, 0, 0, 0, 1]
