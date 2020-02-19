#!/usr/bin/python
# Stock Prices

# You want to write a bot that will automate the task of day-trading for you while you're going through Lambda. You decide to have your bot just focus on buying and selling Amazon stock. 

# Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

# For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices. 

# ## Testing

# Run the test file by executing `python test_stock_prices.py`.

# You can also test your implementation manually by executing `python stock_prices.py [integers_separated_by_a_single_space]`

# ## Hints

#  For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices. 

#  So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`? 


# 1.input list of stock prices
# 2. return maximum profit by subtracting largest price from smallest price- BUT smallest price most come BEFORE largest price
#loop through prices. 
# [50, 200, 1, 10, 30, 40, 35]
# could do: 50 - 20= 30, 50 - 10 = 30, 50 - 100= -50. iterate through each umber subtracting numbers after to find biggest positive difference.
#find the smallest price and minus from biggest price.
#we don't care about the last price for finding smallest price beacsue we can't minus a larger price from it

#loop through array -1 finding the smallest price 
#loop through the array starting at smallest price finding biggest price 

# [50, 200, 1, 10, 30, 40, 35]
    # min_price = 0
    # max_price = (len(prices)-1)
# i count =

import argparse

def find_max_profit(prices):
    min_price = 0
    max_price = (len(prices)-1)

#loop through array finding the smallest price 

    for i in range(len(prices)-1):
        if prices [i] < prices[min_price]:
            min_price = i

#loop through the array starting after min price finding the biggest price 

    for i in range(min_price+1, len(prices)):
        if prices[max_price]<prices[i]:
            max_price = i


#max price minus min price
    return prices[max_price] - prices[min_price]
  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))