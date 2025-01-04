class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums) // 2
        elements = set(nums)
        for element in elements:
            if nums.count(element) > length:
                return element

# RT: 6 ms Beats 73.80; Memory: 13.60 MB Beats 27.57%