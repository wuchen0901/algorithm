from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)

        for booking in bookings:
            diff[booking[0] - 1] += booking[2]
            diff[booking[1]] -= booking[2]
            # 10, 0, -10
            # 10, 20, -10, -20
            # 10, 45, -10, -20, 0, -25

        result = [0] * n
        result[0] = diff[0]
        for i in range(1, n):
            result[i] = result[i - 1] + diff[i]

        return result


if __name__ == '__main__':
    print(Solution().corpFlightBookings(
        [
            [1, 2, 10],
            [2, 3, 20],
            [2, 5, 25]
        ], 5))
