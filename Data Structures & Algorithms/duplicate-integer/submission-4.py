class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = set(nums)
        if len(nums) != len(m):
            return True
        return False