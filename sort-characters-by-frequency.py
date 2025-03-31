"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        char_counts = {}
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
        count_tuples = [(k, v) for k, v in char_counts.items()]
        count_tuples.sort(key=lambda x: (-x[1]))
        sorted_chars = []
        for char, count in count_tuples:
            sorted_chars.extend([char] * count)
        return ''.join(sorted_chars)
        

"""
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
"""

s = "tree"
solution = Solution()
result = solution.frequencySort(s)
print(result)  # Expected output: "eert" or "eetr"