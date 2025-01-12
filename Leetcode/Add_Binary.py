class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_int = int(a, 2)
        b_int = int(b, 2)

        summation = a_int + b_int
        binary = bin(summation)
        string = binary[2:]
        
        return string
    
# RT: 0 ms, Beats 100.00%; Memory: 12.59 MB, Beats 7.34%