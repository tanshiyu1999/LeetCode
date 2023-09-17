class Solution(object):
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    l, r = 0, len(height) - 1
    res = 0
    while l < r:
      distance = r - l 
      shortest = min(height[l], height[r])
      area = distance * shortest  
      res = max(res, area)
      if height[l] <= height[r]:
        l += 1
      else:
        r -= 1
    
    return res
        

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))