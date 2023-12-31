# 67. Add Binary
def addBinary(a: str, b: str) -> str:
    a, b = list(a), list(b)
    temp = 0
    result = []

    while a and b:
        sum = int(a.pop()) + int(b.pop()) + temp
        temp = 0

        if sum == 3:
            temp += 1
            result.append("1")
        elif sum == 2:
            temp += 1
            result.append("0")
        elif sum == 1:
            result.append("1")
        else:
            result.append("0")
    
    if a:
        while a:
            sum = int(a.pop()) + temp
            temp = 0

            if sum == 2:
                temp += 1
                result.append("0")
            elif sum == 1:
                result.append("1")
            else:
                result.append("0")
        if temp:
            result.append("1")

    elif b:
        while b:
            sum = int(b.pop()) + temp
            temp = 0

            if sum == 2:
                temp += 1
                result.append("0")
            elif sum == 1:
                result.append("1")
            else:
                result.append("0")
        if temp:
            result.append("1")
    
    else:
        if temp:
            result.append("1")
    
    return ''.join(reversed(result))

a, b = "1111", "1111"
print(addBinary(a, b)) # 11110