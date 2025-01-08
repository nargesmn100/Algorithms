class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False
        if len(s) == 0: # Edge case!
            return True

        s_list = list(s)
        t_list = list(t)

        # Go through s by means of indexing
        s_index = 0
        
        for i in range(0, len(t)):
            if t_list[i] == s_list[s_index]:
                s_index += 1
            if s_index == len(s):
                return True
        return False
    
# RT: 4 ms, Beats 18.06%; Memory: 13.02 MB Beats 5.59%