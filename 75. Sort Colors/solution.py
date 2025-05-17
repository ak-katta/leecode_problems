class Solution:
    def sortColors(self, nums: List[int]) -> None:

        n=len(nums)
        zero_pos=0      #first pointet (store index where '1' goes)
        two_pos=n-1     #second pointer (store index where '2' goes)
        i=0

        while i <= two_pos:
            if nums[i]==0:
                nums[i],nums[zero_pos]=nums[zero_pos],nums[i]  #swapping elements so that '2' can be come first in list
                zero_pos+=1
                i+=1

            elif nums[i]==2:
                nums[i],nums[two_pos]=nums[two_pos],nums[i]    #swapping elements so that '2' can be come first in list
                two_pos=two_pos-1

            elif nums[i]==1:
                i+=1

        return nums
