class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # .strip() removes excess spaces at the beginning and at the end of the string
        new_list = s.strip().split(" ")
        return len(new_list[-1])
    
    # RT: 0 ms, Beats 100.00%; Memory: 12.58 MB Beats 19.41%