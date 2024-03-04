class Solution:
    def isValid(self, s: str) -> bool:
        pars = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)
                continue
            elif not stack or stack[-1] != pars[c]:
                return False

            stack.pop()

        return not stack

# time: O(n)
# space: O(n)
