class Solution:
    def romanToInt(self, s: str) -> int: #two positional arguements
        dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} #define the romans in key value pairs
        total = 0
        for i in range(len(s) - 1): 
            if dictionary[s[i]] < dictionary[s[i + 1]]: #if the roman number in front is greater like IV I<V then we substract
                total -= dictionary[s[i]]
            else:
                total += dictionary[s[i]] #if the roman number in front is smaller like VI V>I then we add
        return total + dictionary[s[-1]]

#https://www.youtube.com/watch?v=tsmrUi5M1JU
