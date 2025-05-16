class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output=[]  #create an empty array to store the result

        for i in range(len(prices)):      #selecting a array element
            discount = False
            for j in range(i+1,len(prices)):   #selectiong next and their next elements for comparison

                if prices[i] >= prices[j]:
                    output.append(prices[i]-prices[j])   #append the output array if condition meet and discount is applied
                    discount = True
                    break
            
            if not discount:     #if next smaller element is not present, we simply write the respective element
                output.append(prices[i])

        
        return output
