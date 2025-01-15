from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rans_count = Counter(ransomNote) # Counts every letter and tells you how many of each letter there is in (letter, count) format
        mags_count = Counter(magazine)

        for letter, count in rans_count.items(): # To access (letter, count) in dictionary format
            # Access count of letter in magazine dictionary and compare it with the count of that letter in ransom
            if mags_count[letter] < count:
                return False
        
        return True
    
# Runtime: 54 ms, Beats 28.39%; Memory: 12.67 MB, Beats 42.72%