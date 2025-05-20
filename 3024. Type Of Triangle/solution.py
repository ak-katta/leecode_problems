class Solution:
    def triangleType(self, nums: List[int]) -> str:
        i=0
        if nums[i]==nums[i+1]==nums[i+2]:   #if all sides are equal : equilateral triangle
            return "equilateral"

        elif nums[i]==nums[i+1] or nums[i]==nums[i+2] or nums[i+1]==nums[i+2]:     #if two sides are equal and for every side a+b>c, this proves that it is a valid triangle  
            if nums[i]+nums[i+1]>nums[i+2] and nums[i]+nums[i+2]>nums[i+1] and nums[i+1]+nums[i+2]>nums[i]:
                return "isosceles"
            else: 
                return "none"

        elif nums[i]+nums[i+1]>nums[i+2] and nums[i]+nums[i+2]>nums[i+1] and nums[i+1]+nums[i+2]>nums[i]:    #swm of any two side must be greater than the third is scalene triangle
            return "scalene"           
                
        else:
            return "none"
               
