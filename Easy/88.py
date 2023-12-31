# 88. Merge Sorted Array
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for num2 in nums2:
        for ptr in range(0, len(nums1)):
            if num2 < nums1[ptr]:
                temp = nums1[ptr]
                for idx in range(ptr, len(nums1) - 1):
                    nums1[idx+1], temp = temp, nums1[idx+1]
                nums1[ptr] = num2
                m += 1
                break
            elif ptr == m:
                nums1[ptr] = num2
                m += 1
                break
                    
                
nums1, m, nums2, n =[4,5,6,0,0,0], 3, [1,2,3], 3
merge(nums1, m, nums2, n)
print(nums1)
