class Solution(object):
    def isValid(self, s):
        stack = []
        # Pairs that map each closing bracket to their respective opening
        pairsMap = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for char in s:
            if char in pairsMap:
                if not stack or stack[-1] != pairsMap[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return not stack
        