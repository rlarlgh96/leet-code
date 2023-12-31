# 69. Sqrt(x)
def mySqrt(x: int) -> int:
    i = 1

    while x >= i * i:
        i += 1
    
    return i - 1

x = 8
print(mySqrt(x)) # 2