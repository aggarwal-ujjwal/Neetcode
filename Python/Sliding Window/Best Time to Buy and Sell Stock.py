class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ans = 0
        minNum = sys.maxsize

        for price in prices:
            minNum = min(minNum,price)
            ans = max(ans, price - minNum)

        return ans

#For most practical purposes, sys.maxsize serves as a suitable substitute for INT_MAX in Python.

#Kadane's Algorithm
#the logic is to calculate the difference (maxCur += prices[i] - prices[i-1]) of the original array, and find a contiguous subarray giving maximum profit. If the difference falls below 0, reset it to zero.