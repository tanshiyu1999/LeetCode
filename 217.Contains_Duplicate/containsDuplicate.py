class Solution(object):
  def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    """
    # Time complexity: O(nums)
    # Space complexity: O(nums)
    # However, this code will run out of time
    hash = {}
    for i in nums:
      if i in hash.keys():
        return True
      else:
        hash[i] = 0
    return False
    """
    hashSet = set()
    for n in nums: 
      if n in hashSet:
        return True 
      hashSet.add(n)
    return False


s = Solution()
print(s.containsDuplicate([1,2,3,4,5,6,7,8]))
    