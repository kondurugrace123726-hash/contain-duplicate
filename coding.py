""" Return True if the array contains duplicate elements
Time Complexity : O(n)
Space Complexity : O(n)"""

class Solution:
    def contains_duplicates(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add (num)
        return False
nums = [1, 2, 5, 2, 9,]
sol = Solution()
print(sol.contains_duplicates(nums))