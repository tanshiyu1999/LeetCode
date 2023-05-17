import re
class Solution(object):
  def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """


    newS = re.sub(r'[\W_]', '', s).lower()
    reversedNewS = newS[::-1]
    return newS == reversedNewS
    
    


s = Solution()
print("Output: ", s.isPalindrome("A man, a plan, a canal: Panama"))