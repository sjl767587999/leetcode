nums = [1,1,2]
nums_len = len(nums)
i = 1
while i<nums_len:
    if nums[i]==nums[i-1]:
        nums.remove(i)
        nums_len = nums_len - 1
    else:
        i = i+1
for i in nums:
    print(i)
