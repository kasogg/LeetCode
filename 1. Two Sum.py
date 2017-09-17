class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        loopmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in loopmap.keys():
                return [loopmap[complement], i]                
            loopmap[nums[i]] = i

print Solution().twoSum([2, 7, 11, 15], 9)