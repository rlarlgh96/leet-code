# 136. Single Number
def singleNumber(nums: list[int]) -> int:
    nums.sort()
    pnt = 0

    while pnt < len(nums) - 1:
        if nums[pnt] != nums[pnt+1]:
            return nums[pnt+1]
        else:
            pnt += 2
    
    return nums[pnt]

nums = [4,1,2,1,2]
print(singleNumber(nums))