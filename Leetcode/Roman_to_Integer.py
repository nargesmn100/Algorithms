class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # REMEMBER COMMAS
        roman_numeral_to_int = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        total = 0

        # If the Roman numeral isn't written from largest to smallest from left to right 
        # (i.e. left number is smaller than right number, subtract the left number from the right number)
        
        list_of_roman_strings = list(s)
        for i in range(len(list_of_roman_strings)):
            dictionary_val = roman_numeral_to_int[list_of_roman_strings[i]]
            if i < len(list_of_roman_strings) - 1 and dictionary_val < roman_numeral_to_int[list_of_roman_strings[i + 1]]:
                total -= dictionary_val
            else:
                total += dictionary_val
        return total
    
    # RT: 19 ms, Beats 15.34%; Memory: 12.51 MB Beats 18.34%