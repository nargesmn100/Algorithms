class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Note that strings in Python are immutable
        s_lst = []
        for i in range(0, len(s)):
            if s[i].isalnum():
                s_lst.append(s[i].lower())
        return s_lst[::-1] == s_lst
    
# RT: 15 ms, Beats 64.32%; Memory: 17.48 MB Beats 5.24%