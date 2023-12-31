# 13. Roman to Integer
def romanToInt(s: str) -> int:
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    n = len(s)

    for idx in range(0, n-1):
        if dict[s[idx+1]] <= dict[s[idx]]:
            result += dict[s[idx]] 
        else:
            result -= dict[s[idx]]
    
    result += dict[s[-1]]

    return result

s = "LVIII"
print(romanToInt(s)) # 58