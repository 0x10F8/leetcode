"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

class Solution:

    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums) - 1)


    def quicksort(self, nums:list[int], start: int, end: int) -> None:
        if start < end:
            pivot_index = self.partition(nums, start, end)
            self.quicksort(nums, start, pivot_index - 1)
            self.quicksort(nums, pivot_index + 1, end)

    def partition(self, nums:list[int], start: int, end: int) -> int:
        pivot = nums[end]
        i = start - 1
        for j in range(start, end):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[end] = nums[end], nums[i + 1]
        return i + 1

"""
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

"""

nums = [2,0,2,1,1,0]
solution = Solution()
solution.sortColors(nums)
print(nums)  # Expected output: [0,0,1,1,2,2]