# this is really bad implementation tho
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in {'[', '{', '('}:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if not((p == '[' and c == ']') or (p == '(' and c == ')') or (p == '{' and c == '}')):
                    return False

        if len(stack) == 0:
            return True
        return False

