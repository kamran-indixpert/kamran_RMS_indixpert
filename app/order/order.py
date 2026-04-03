from app.database.db import Data
from app.menu.menu import Menu
import uuid

class Order:

    def take_order(self):

        try:
            menu_obj = Menu()
            menu_obj.view()

            
            try:
                item_id = int(input("\nEnter Item ID: "))
            except ValueError:
                print(" Invalid ID")
                return

            item = menu_obj.get_item_by_id(item_id)

            if not item:
                print(" Item not found")
                return

            
            plate = input("Plate (half/full): ").lower()
            if plate not in ["half", "full"]:
                print(" Invalid plate")
                return

            
            try:
                qty = int(input("Quantity: "))
            except ValueError:
                print(" Invalid quantity")
                return

            if qty <= 0:
                print(" Quantity must be > 0")
                return

            
            full_price = item["price"]
            half_price = full_price / 2

            price = half_price if plate == "half" else full_price
            total = price * qty

            
            name = item["name"].lower()

            if any(x in name for x in ["chicken", "egg", "fish", "prawn"]):
                category = "non-veg"
            elif any(x in name for x in ["fries", "momos", "roll", "soup", "tikka", "wings"]):
                category = "starter"
            elif any(x in name for x in ["drink", "coffee", "tea", "shake", "lassi", "water", "ice cream", "cake", "pastry"]):
                category = "drinks"
            else:
                category = "veg"

            
            orders = Data.read(Data.ORDER_PATH)

            order_id = str(uuid.uuid4())[:8]

            order_data = {
                "order_id": order_id,
                "item": item["name"],
                "category": category,
                "plate": plate,
                "qty": qty,
                "unit_price": price,
                "total": total
            }

            orders.append(order_data)
            Data.write(Data.ORDER_PATH, orders)

            
            print("\n===== ORDER BILL =====")
            print(f"Order ID : {order_id}")
            print(f"Item     : {item['name']}")
            print(f"Category : {category}")
            print(f"Plate    : {plate}")
            print(f"Qty      : {qty}")
            print(f"Price    : ₹{price}")
            print(f"Total    : ₹{total}")
            print("======================")

        except Exception as e:
            print(" Error:", e)


     