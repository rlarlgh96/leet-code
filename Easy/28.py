# 28. Find the Index of the First Occurence in a String
from collections import deque

def strStr(haystack: str, needle: str) -> int:

    if needle not in haystack:
        return -1
    
    for idx in range(0, len(haystack)):
            if haystack[idx] == needle[0]:
                if haystack[idx:idx+len(needle)] == needle:
                    return idx

haystack, needle = "sadbutsad", "sad"                
print(strStr(haystack, needle)) # 0