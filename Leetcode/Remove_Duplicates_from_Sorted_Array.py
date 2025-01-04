class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_elements = set() # This is how you properly initialize a set, {} is for dictionaries
        copy = nums[:]
        length = len(nums)
        for i in range(len(copy)):
            if copy[i] in unique_elements:
                nums.remove(copy[i])
                length -= 1
            else:
                unique_elements.add(copy[i])
        return length

# This solution works because we are not modifying the list while iterating, so no unexpected behaviour is caused. 

# RT: 90 ms Beats 6.90%; Memory: 14.18 MB Beats 10.29%