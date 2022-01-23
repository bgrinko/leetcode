"""LeetCode problem 150. Evaluate Reverse Polish Notation

Link:       https://leetcode.com/problems/evaluate-reverse-polish-notation/
Difficulty: Medium
Status:     Accepted (01/22/2022 12:47) 75 ms 14.5 MB
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in range(len(tokens)):
            s: str = tokens[t]
            if s not in "+-*/":
                stack.append(int(s))
            else:
                r, l = stack.pop(), stack.pop()
                if s == "+":
                    stack.append(l + r)
                elif s == "/":
                    stack.append(int(l / r))
                elif s == "*":
                    stack.append(l * r)
                else:
                    stack.append(l - r)

        return stack[0]
