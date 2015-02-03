#151
#Reverse Words in a String
#Given an input string, reverse the string word by word.
#
#For example,
#Given s = "the sky is blue",
#return "blue is sky the".

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.split(' ')
        s = [x for x in s if x != '']
        n = len(s)
        for i in range(n/2):
            s[i], s[n-i-1] = s[n-i-1], s[i]
        return ' '.join(s)

if __name__ == '__main__':
    s = Solution()
    str = "  a  b  "
    print s.reverseWords(str)