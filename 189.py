class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[len(nums)-k:len(nums)]+nums[0:len(nums)-k]

list = [1,2,3,4,5,6,7]
r =  Solution()
r.rotate(list,3)
print(r.rotate(list,3))