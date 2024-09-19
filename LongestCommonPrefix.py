from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]    
        for i in range(len(prefix)):
            for word in strs[1:]:
                if ( i ==len(word) or word[i] != prefix[i]):
                    return prefix[0:i]
        return base            
