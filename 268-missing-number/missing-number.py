class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expect = n*(n+1)//2
        actual = 0
        for i in range(len(nums)):
            actual += nums[i]
        return expect - actual