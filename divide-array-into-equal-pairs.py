"""
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.
"""
class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        for num in num_count:
            if num_count[num] % 2 != 0:
                return False
        return True


solution = Solution()
nums = [3, 2, 3, 2, 2, 2]
result = solution.divideArray(nums)
print(result) 