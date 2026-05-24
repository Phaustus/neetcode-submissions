class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nn = n
        while nn != 0:
            nums1.remove(0)
            nn -= 1

        nums1[:] = sorted(nums1[:m] + nums2[:n])



        