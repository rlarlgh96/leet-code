# 58. Lenght of Last Word
def lengthOfLastWord(s: str) -> int:
    s = s.rstrip()
    result = 0

    for idx in range(len(s)-1, -1, -1):
        if s[idx] != ' ':
            result += 1
        else:
            break

    return result

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s)) # 4