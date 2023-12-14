def RemoveFunction(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j

print(RemoveFunction([0, 0, 0, 1, 1, 2, 3, 3, 3]))  

"""def removeDuplicates(self, nums: List[int]) -> int:
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j"""