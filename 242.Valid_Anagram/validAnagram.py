class Solution(object):
  def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # sorted solution has time complexity of the sorting algorithm, likely O(logn)
    # return sorted(s) == sorted(t)

    # Run time of O(s + t)
    # Space Complexity of O(s + t)
    hashS = {}
    hashT = {}
    for letter in s: 
      if letter not in hashS.keys():
        hashS[letter] = 1
      else:
        hashS[letter] = hashS[letter] + 1
        continue
    for letter in t: 
      if letter not in hashT.keys():
        hashT[letter] = 1
      else:
        hashT[letter] = hashT[letter] + 1
        continue
    
    return hashS == hashT
    
s = Solution()
print(s.isAnagram("rat", "tac"))
        