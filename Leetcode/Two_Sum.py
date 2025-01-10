class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = []
        for i in range(0, len(nums)):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] + nums[j] == target:
                    lst.append(i)
                    lst.append(j)
                    return lst
                
# RT: 2064 ms, Beats 31.61%; 13.32 MB, Beats 13.97%