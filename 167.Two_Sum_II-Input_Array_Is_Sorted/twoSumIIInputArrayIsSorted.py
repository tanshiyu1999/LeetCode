class Solution(object):
  def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    last = len(numbers) - 1
    first = 0

    while first != last:
      currSum = numbers[first] + numbers[last]
      if currSum == target:
        return [first + 1, last + 1]
      elif currSum > target:
        last = last - 1
        continue 
      elif currSum < target:
        first = first + 1
        continue
    return []
    
  
s = Solution()
print(s.twoSum([2,7,11,15], 9))
    