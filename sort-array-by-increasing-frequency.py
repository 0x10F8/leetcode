"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.
"""
class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        count_tuples = [(k,v) for k,v in counts.items()]
        count_tuples.sort(key=lambda x: (x[1], -x[0]))
        sorted_nums = []
        for num, count in count_tuples:
            sorted_nums.extend([num] * count)
        return sorted_nums

nums = [1,1,2,2,2,3]
solution = Solution()
result = solution.frequencySort(nums)
print(result)  # Expected output: [3,1,1,2,2,2]