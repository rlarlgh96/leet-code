# 70. Climbing Stairs
import math

def climbStairs(n: int) -> int:
    m = 0 # number of 2 steps
    result = 1

    while n > 0:
        n -= 2
        m += 1

        if n < 0:
            break
        
        result += math.comb(n + m, m)
    
    return result

n = 3
print(climbStairs(n)) # 3