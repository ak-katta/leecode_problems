class Solution:
    def threeConsecutiveOdds(self,arr):
        n=len(arr)
        res=[]
        for i in range (n-2):                                          #loop till n-2 as we take three elements simultaneously
            if (arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0 ):     #checking condition for three consecutive odds
                return True
        
        return False                                                   #return false if not found
            
            
        
        
