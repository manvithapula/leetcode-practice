class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack1.pop() if stack1 else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack1.append(char)
        return not stack1
