prices = {'apple': 10, 'banana': 5, 'orange': 8}
quantity = {'apple': 2, 'banana': 3, 'orange': 1}
total_bill = sum(prices[item] * quantity[item] for item in prices if item in quantity)
