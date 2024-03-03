class Solution:
    def isValid(self, s: str) -> bool:
        dict = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)
                continue
            elif not stack or stack[-1] != dict[c]:
                return False

            stack.pop()

        return not stack

# time: O(n)
# space: O(n)
        