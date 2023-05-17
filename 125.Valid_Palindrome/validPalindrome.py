"""
My answer might be non-standard, as the actual answer uses 2 pointers in order to make the time complexity O(2N)
"""

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