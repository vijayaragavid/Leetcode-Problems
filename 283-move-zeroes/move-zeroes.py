class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res=[]
        
        for i in range(len(nums)):
            if nums[i] != 0:
                res.append(nums[i])
        
        zerocount = nums.count(0)
        for i in range(zerocount):
            res.append(0)
        
        for i in range(len(nums)):
            nums[i]=res[i]
        