class Solution(object):
  def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # Can use bucket sort to make run time better

    # Runtime: O ( nums + k * nums )
    hashMap = {}
    output = []
    for i in nums: # run time is num for this
      if i not in hashMap.keys():
        hashMap[i] = 1
      else:
        hashMap[i] = hashMap[i] + 1

    
    for x in range(k): # run time is k
      if hashMap == {}:
        return output

      max_value = max(hashMap, key=hashMap.get) # This run time is O(n), meaning O ( num )
      output.append(max_value)
      hashMap.pop(max_value)
    
    return output

s = Solution()
s.topKFrequent([], 2)
