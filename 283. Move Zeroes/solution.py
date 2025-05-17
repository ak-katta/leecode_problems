class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_pos = 0          #This stores non zero element position where next non zero element to be stored
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]        #swapping numbers with non zero position and nums[i]
                non_zero_pos += 1
