from typing import List

def removeElement(nums: List[int], val: int) -> int:
    cnt = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[cnt] = nums[i]
            cnt += 1w
    return cnt

ans = removeElement([3,2,2,3], 3)

print(ans)