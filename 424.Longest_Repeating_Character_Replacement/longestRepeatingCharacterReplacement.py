# My solution works on local computer but not online?
class Solution(object):
  def characterReplacement(self, s, k):
    hash = {}
    res = 0
    l = 0 
    r = 0

    s = [char for char in s]
    hash[s[0]] = 1

    while r < len(s) - 1:      
      allValues = hash.values()
      maxValue = max(allValues)
      
      numberOfDigits = r - l + 1
      numberOfDuplicate = numberOfDigits - maxValue

      if numberOfDuplicate > k:
        hash[s[l]] -= 1
        l += 1
      else:
        r += 1
        if hash.get(s[r]) is None:
          hash[s[r]] = 1
        else:
          hash[s[r]] += 1  
      
      maxValue = max(allValues)
      numberOfDigits = r - l + 1
      numberOfDuplicate = numberOfDigits - maxValue
      if (numberOfDuplicate > k):
        hash[s[l]] -= 1
        l += 1
      res = max( (r - l + 1),  res)
      print("r: ", r)
      print("l: ", l)
      print("hash: ", hash)
      print("res: ", res)
      print("----")
    print("res: ", res) 
    return res 
  
s = Solution()
s.characterReplacement("ABABAABA", 2)
