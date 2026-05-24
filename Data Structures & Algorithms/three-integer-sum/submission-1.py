class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        nums.sort()
        for k in range(len(nums)):
            if k != 0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = len(nums) - 1

            while i < j:
                if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in l:
                    l.append([nums[i], nums[j], nums[k]])

                if nums[i] + nums[j] + nums[k] > 0:
                    j -= 1
                else:
                    i += 1
        return l
                


                