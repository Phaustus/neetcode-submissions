class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        b = {0: 0, 1: 0, 2: 0}
        r = []

        for i in nums:
            if i in b:
                b[i] += 1

        nums[:] = [j for j in range(len(b)) for _ in range(b[j])]



        