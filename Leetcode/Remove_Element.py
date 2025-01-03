class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for value in nums:
            if value == val:
                nums.remove(value)
        return len(nums)