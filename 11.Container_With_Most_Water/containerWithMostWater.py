class Solution(object):
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    w = len(height)
    l = height[0]
    r = height[-1]
    h = min(height[r], height[l])


    currRight = len(height) - 1
    currLeft = 0
    currWidth = len(height)

    while currWidth != 0:
      currWidth-=1
      if currRight == currLeft:
        break
      if currRight > currLeft:
        currRight-=1
        if height[currRight] - h > w - currWidth:
          r = currRight
          h = min(height[r], height[l])
          w = r - l
      else:
        left+=1
        if (height[currLeft] - h) > w - currWidth:
          l = currLeft
          h = min(height[r], height[l])
          w = r - l

    
    print("width: ", w)
    print("height: ", h)
    return w * h

      

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))