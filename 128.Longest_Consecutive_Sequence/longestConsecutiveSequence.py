"""
my solution is only O(nlogn), but we can do better.

Optimal solution:
https://www.youtube.com/watch?v=P6RZZMu_maU&ab_channel=NeetCode

"""

class Solution(object):
  def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sortedNums = sorted(nums)
    longest = 0
    currLongest = 1
    totalNum = len(sortedNums)

    if totalNum == 0:
      return 0

    for count, num in enumerate(sortedNums):
      if count + 1 >= totalNum:
        if currLongest > longest:
          longest = currLongest
        break

      if num == sortedNums[count + 1] - 1:
        currLongest+=1
        # print("current num ", num)
        # print("currLongest, ", currLongest)
        # print("-------------------------------")
        continue
      elif num == sortedNums[count + 1]:
        continue
      else:
        if currLongest > longest:
          longest = currLongest
          currLongest = 1
          continue
        else:
          currLongest = 1
          continue
    
    # print(longest)
    return longest
    
      
      


s = Solution()
s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])