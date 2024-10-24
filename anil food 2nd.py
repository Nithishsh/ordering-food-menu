def calculate_total():
    menu = {
        1: {"item": "Pizza", "price": 200},
        2: {"item": "Burger", "price": 100},
        3: {"item": "Dosa", "price": 150},
        4: {"item": "Briyani", "price": 250},
        5: {"item": "Chicken rice", "price": 200}
    }

    print("Menu:")
    for key, value in menu.items():
        print(f"{key}. {value['item']} - Rs.{value['price']}")

    choice = int(input("Enter your choice (1-5): "))
    quantity = int(input("Enter quantity: "))

    selected_item = menu[choice]
    total_cost = selected_item["price"] * quantity

    if total_cost > 500:
        discount = total_cost * 0.1
        total_cost -= discount
        print(f"A 10% discount has been applied. Discount: Rs.{discount}")

    return total_cost
