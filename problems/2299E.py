"""LeetCode problem 2299. Strong Password Checker II

Link:       https://leetcode.com/problems/strong-password-checker-ii/
Difficulty: Easy
Status:     Accepted (07/01/2022 13:30) 62 ms 14 MB
"""


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        last = '~'

        low = False
        up = False
        dig = False
        spec = False

        for i in password:
            if i == last:
                return False
            last = i
            if i in string.ascii_lowercase:
                low = True
            elif i in string.ascii_uppercase:
                up = True
            elif i in string.digits:
                dig = True
            elif i in '!@#$%^&*()-+':
                spec = True

        return low and up and dig and spec
