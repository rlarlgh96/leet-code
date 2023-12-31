# 26. Remove Duplicates from Sorted Array
from collections import defaultdict

def removeDuplicates(nums: list[int]) -> int:
    temp = defaultdict(int)

    for num in nums:
        temp[num] += 1

    for i in temp.keys():
        for j in range(0, temp[i]-1):
            nums.remove(i)
    
    return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums)) # 5