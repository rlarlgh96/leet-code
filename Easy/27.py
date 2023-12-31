# 27. Remove Element
def removeElement(nums: list[int], val: int) -> int:
    
    while val in nums:
        nums.remove(val)

    return len(nums)

nums, val = [3,2,2,3], 3
print(removeElement(nums, val)) # 2