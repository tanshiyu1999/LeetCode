class Solution(object):
  # This solution is O(n), since it is implementating a hashmap
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # So Apparently python dictionary is literally a hashmap
    hashMap = {}
    currentIndex = 0
    for i in nums:
      if (target - i) in hashMap.keys():
        return [hashMap[target - i], currentIndex]
      else:
        hashMap[i] = currentIndex
        currentIndex = currentIndex + 1
    return []

s = Solution()
print(s.twoSum([1,2,3], 3))