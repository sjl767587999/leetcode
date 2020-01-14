class Solution(object):
    def maxProfit(self, prices):
        result = 0
        for i in range(1, len(prices)):
            k = prices[i] - prices[i - 1]
            if k > 0:
                result = result + k
        return result

list = [7,1,5,3,6,4]
r =  Solution()
print(r.maxProfit(list))