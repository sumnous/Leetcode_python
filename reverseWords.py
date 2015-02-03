#186
#Reverse Words in a String II
#
#Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
#
#The input string does not contain leading or trailing spaces and the words are always separated by a single space.
#
#For example,
#Given s = "the sky is blue",
#return "blue is sky the".
#
#Could you do it in-place without allocating extra space?

class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        n = len(s)
        for i in range(n/2):
            s[i],s[n-i-1] = s[n-i-1],s[i]
        i = 0; num = 0
        while i < n:
            if s[i] != ' ':
                i += 1; num += 1
            else:
                for j in range(num/2):
                    s[i-num+j],s[i-j-1] = s[i-j-1],s[i-num+j]
                i += 1; num = 0
        for j in range(num/2):
            s[i-num+j],s[i-j-1] = s[i-j-1],s[i-num+j]

if __name__ == '__main__':
    s = Solution()
    str = "the sky is blue"
    s.reverseWords(list(str))

