class Solution:
    def scoreOfString(self, s: str) -> int:
        total_sum = 0
        for i in range(1, len(s)):
            convertToAscii = ord(s[i])
            convertToAscii1 = ord(s[i - 1])
            absofascii = abs(convertToAscii - convertToAscii1)  
            total_sum += absofascii  
        return total_sum
