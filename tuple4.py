food_items = [("Burger", 120), ("Pizza", 300), ("Sandwich", 150)]
sorted_food = sorted(food_items, key=lambda x: x[1], reverse=True)
print(sorted_food)

