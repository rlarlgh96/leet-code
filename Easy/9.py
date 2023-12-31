# 9. Palindrome Number
def isPalindrome(x: int) -> bool:
        x = str(x)
        n = len(x)

        for i in range(0, n // 2):
            if x[i] != x[n-i-1]:
                return False

        return True

x = 121
print(isPalindrome(x)) # True