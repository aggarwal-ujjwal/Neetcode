class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]

#isalnum - is both in C++ and Python
#Write a solution wrt to two pointers