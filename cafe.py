menu={
       "tea": 120,
       "coffee": 200,
       "sandwich": 450,
       "cookie": 150,
       "cake_slice": 320
}

inventory={
       "tea": 40,
       "coffee": 35,
       "sandwich": 20,
       "cookie": 50,
       "cake_slice": 25
}

orders = [
    {"tea": 2, "cookie": 1},
    {"coffee": 1, "sandwich": 2},
    {"tea": 3, "cake_slice": 1},
    {"coffee": 2, "cookie": 2, "sandwich": 1},
    {"tea": 1},
    {"coffee": 1, "cake_slice": 2}
]

sold_item={item:0 for item in menu}
order_totals = []

for i in range(len(orders)):
    print(f"\nOrder {i+1}:")
    order = orders[i]
    total_price = 0

    for item in order:
        if item in menu:
            quantity = order[item]

            if quantity <= inventory[item]:
                inventory[item] -= quantity
                sold_item[item] += quantity
                price = menu[item] * quantity
                total_price += price
                print(f"ordered {quantity} {item} | Bill = Rs.{price}")
            else:
                print(f"sorry, only {inventory[item]} {item} available")
    order_totals.append(total_price)
    print(f"Order Total = Rs.{total_price}")

print("\nEnd of Day Summary")
print(f"{'Item':15} {'Sold':5} {'Price/unit':10} {'Revenue':10} {'Stock Left':10}")

total_revenue = 0

for item in menu:
    sold = sold_item[item]
    revenue = sold * menu[item]
    total_revenue += revenue
    print(f"{item:15} {sold:<5} {menu[item]:<10} {revenue:<10} {inventory[item]:<10}")

print(f"\nTotal Revenue of the Day = Rs. {total_revenue}")
