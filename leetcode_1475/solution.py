class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output = []

        for i in range(len(prices)):
            discount = False
            for j in range(i + 1, len(prices)):

                if prices[i] >= prices[j]:
                    output.append(prices[i] - prices[j])
                    discount = True
                    break

            if not discount:
                output.append(prices[i])

        return output