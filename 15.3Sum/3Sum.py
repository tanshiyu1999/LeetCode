class Solution(object):
  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums = sorted(nums)
    hashMap = {}
    for num in nums:
      hashMap[num] = 0
    
    print(nums)
    total = len(nums)
    back = 0
    front = 1
    
    # first loop, smallest value
    while front != back:
      sum = front + back
      
    
s = Solution()
s.threeSum([-1,0,1,2,-1,-4])