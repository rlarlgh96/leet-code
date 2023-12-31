# 66. Plus One
def plusOne(digits: list[int]) -> list[int]:
    temp = ""

    for number in digits:
        temp += str(number)
    
    temp = str(int(temp) + 1)

    return [int(temp[i]) for i in range(len(temp))]

digits = [1,2,3]
print(plusOne(digits)) # [1,2,4]