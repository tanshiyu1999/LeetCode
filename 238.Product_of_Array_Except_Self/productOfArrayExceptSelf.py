class Solution(object):
  def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    total = 1
    doesZeroExist = False
    # If 2 zeroes exist, then the nums list will be 0
    # If only 1 0 exist, then only the value with 0 will have the total value, and the rest of the variables will have 0
    doesTwoZeroExist = False
    for num in nums: 
      if num == 0:
        if doesZeroExist == True:
          doesTwoZeroExist = True
        doesZeroExist = True
        continue
      total = total * num
        
    for count, num in enumerate(nums):
      if doesTwoZeroExist == True:
        nums[count] = 0
        continue

      if num == 0:
        nums[count] = total
      else:
        if doesZeroExist == True:
          nums[count] = 0
          continue
        nums[count] = total/num 
    
    print(nums)
    return nums
  
s = Solution()
s.productExceptSelf([0, 0])
