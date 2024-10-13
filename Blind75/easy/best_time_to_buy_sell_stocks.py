"""
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
    
                                                                                                        X
    Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104
    
"""

# [7,1,5,3,6,4]


def max_profit_ptr(prices):
    """
    Time: O(n log n) because list iteration is cut in half by moving the pointers incrementally
    Space: O(1)
    """
    max_profit = 0
    buy_ptr = 0
    sell_ptr = 1

    while buy_ptr != len(prices) - 1:
        potential_profit = prices[sell_ptr] - prices[buy_ptr]
        if potential_profit > max_profit:
            max_profit = potential_profit
        sell_ptr += 1
        if sell_ptr > len(prices) - 1:
            buy_ptr += 1
            sell_ptr = buy_ptr + 1

    return max_profit


if __name__ == "__main__":
    assert max_profit_ptr([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit_ptr([7, 6, 4, 3, 1]) == 0
    assert max_profit_ptr([9, 1, 3, 19, 8, 32, 4, 5]) == 31
