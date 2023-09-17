class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        longest = 0
        hash = {}
        
        for i, c in enumerate(s):
            if c == " ":
                continue
            elif hash.get(c) == None:
                hash[c] = i
            elif hash[c] < start:
                hash[c] = i
            else:
                toBeReplaced = hash[c]
                currLength = i - toBeReplaced
                longest = max(currLength, longest)
                hash[c] = i 
                start = max(start, i)
            
        return longest
    
    #NOT DONE


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
        