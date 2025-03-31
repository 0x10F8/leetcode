"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        count_tuples = [(num, count) for num, count in num_count.items()]
        count_tuples.sort(key=lambda x: x[1], reverse=True)
        top_k = count_tuples[:k]
        return [num for num, _ in top_k]

"""
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

nums = [1,1,1,2,2,3]
k = 2
solution = Solution()
result = solution.topKFrequent(nums, k)
print(result)  # Expected output: [1,2] or [2,1]