class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    currSmallest = prices[0]
    currLargest = prices[0]

    for price in prices:
      if price < currSmallest:
        currSmallest = price
        currLargest = price
      if price > currLargest:
        currLargest = price
      if (currLargest - currSmallest > profit):
        profit = currLargest - currSmallest
      
      
    return profit 

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))