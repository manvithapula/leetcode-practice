leetcode 9
class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0: #negative cant be palindrome
      return False
    rev = 0 #Initializes rev to store the reversed number.
    y = x #manipulate value
    while y:
      rev = rev * 10 + y % 10 #Adds the last digit of y to rev, building the reversed number.
      y //= 10
    return rev == x 
