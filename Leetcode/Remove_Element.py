class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        copy = nums[:]
        length = len(nums)
        for i in range(0, len(copy)):
            if copy[i] == val:
                nums.remove(val)
                length -= 1
        return length
    
# RT: 0ms, Beats 100.00%; Memory: 12.56 MB Beats 12.98%