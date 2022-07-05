"""LeetCode problem 29. Divide Two Integers

Link:       https://leetcode.com/problems/divide-two-integers/
Difficulty: Medium
Status:     Accepted (07/05/2022 20:32) 51 ms 13.9 MB
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def magic(dividend, divisor):
            if divisor > dividend:
                return 0
            result = 1
            target = divisor
            n = 0
            while n < 10:
                pl = divisor
                k = 1

                while target < dividend:
                    target += pl
                    pl <<= 1
                    result += k
                    k <<= 1

                mi = divisor
                l = 1

                while target > dividend:
                    target -= mi
                    mi <<= 1
                    result -= l
                    l <<= 1

                if dividend - target < divisor:
                    break

                n += 1

            if dividend - target < divisor:
                return result
            else:
                while target < dividend - divisor:
                    target += divisor
                    result += 1

            return result

        sign = True

        if dividend < 0:
            dividend = -dividend
            sign = not sign

        if divisor < 0:
            divisor = -divisor
            sign = not sign

        result = magic(dividend, divisor)

        if not sign:
            result = -result

        if result > 2**31 - 1:
            return 2**31 - 1

        if result < -2**31:
            return -2**31

        return result
