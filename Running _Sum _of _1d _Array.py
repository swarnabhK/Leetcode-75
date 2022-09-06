class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        windowSum = 0
        for i in range(len(nums)):
            windowSum+=nums[i]
            nums[i] = windowSum
        return nums