from collections import defaultdict

class Solution(object):
  def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    # O( m * n * 26 ) -< O ( m * n )
    # where m is the number of total input string
    # wherer n is the average length of each string
    # for going through count
    result = defaultdict(list) # mapping charCount to list of Anagrams

    for s in strs:
      count = [0] * 26 # a ... z
      for c in s:
        count[ord(c) - ord("a")] += 1 # this is using ascii value
      # here, count became a 
      
      result[tuple(count)].append(s)
    

    return result.values()



    """
    # My solution, it does not work
    # I cannot figure out how to reference the values properly.
    hashMap = {}
    hashMapSorted = []
    uniqueAnagrams = 0
    # first sort them out.
    for count, str in enumerate(strs):
      sortedList = sorted(str)
      sortedStr = ''.join(sortedList)
      if sortedStr not in hashMapSorted.keys():
        hashMapSorted[sortedStr] = uniqueAnagrams
        hashMap[str] = uniqueAnagrams
        uniqueAnagrams+=1
      elif sortedStr in:
        hashMapSorted[sortedStr] = hashMapSorted[sortedStr]
    
    for key in hashMap:
      if hashMap[key] in 

    """

s = Solution()
s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    
      