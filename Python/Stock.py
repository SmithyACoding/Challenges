'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Create the best price to buy at and the profit
        bestPrice = prices[0]
        profit = 0
        #Check the next items in the list
        for price in prices[1:]:
            #if the current price is less than the best price
            if price < bestPrice:
                #update the new best price
                bestPrice = price

            #check if there's more profit with this price
            if profit < price - bestPrice:
                #update the new profit
                profit = price - bestPrice

        return profit

                
