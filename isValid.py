class Solution:
    # @return a boolean
    def isValid(self, s):
        if s == '':
            return True
        left = '([{'
        right = ')]}'
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
                continue
            for j in xrange(3):
                if i == right[j]:
                    if not stack or stack[-1] != left[j]:
                        return False
                    else:
                        stack.pop()
                        continue
        return not stack

s = Solution()
print s.isValid('()')