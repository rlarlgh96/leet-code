# 20. Vaild Parentheses
def isValid(s: str) -> bool:
    dict = {'(': ')', '[': ']', '{': '}'}
    temp = []
    
    for i in s:

        if i in dict:
            temp.append(dict[i])
        else:
            if temp:
                if i == temp.pop():
                 continue
                else:
                    return False
            else:
                return False
    
    if len(temp) == 0:
        return True
    else:
        return False

s = "()[]{}"
print(isValid(s)) # True
