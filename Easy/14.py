# 14. Longest Common Prefix
import math

def longestCommonPrefix(strs: list[str]) -> str:
    m = math.inf

    for i in strs:
        if len(i) < m:
            word = i
    
    strs.remove(word)
    result = ""
    
    for ptr in range(len(word), 0, -1):
        cnt = 0

        for i in strs:
            if word[:ptr] == i[:ptr]:
                cnt += 1
                
        if cnt == len(strs):
            result = word[:ptr]
            break
    
    
    return result

strs = ["flower","flight","flow"]
print(longestCommonPrefix(strs)) # fl
