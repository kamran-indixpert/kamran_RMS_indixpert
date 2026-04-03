from app.database.db import Data

class Menu:

    def view(self):

        menu = Data.read(Data.MENU_PATH)

        if not menu:
            print(" Menu empty")
            return

        veg = []
        nonveg = []
        starter = []
        drinks = []

        for m in menu:
            name = m["name"].lower()

            if any(x in name for x in ["chicken", "egg", "fish", "prawn","omelette"]):
                nonveg.append(m)

            elif any(x in name for x in ["fries", "momos", "roll", "soup", "tikka", "wings"]):
                starter.append(m)

            elif any(x in name for x in ["drink", "coffee", "tea", "shake", "lassi", "water", "ice cream", "cake", "pastry"]):
                drinks.append(m)

            else:
                veg.append(m)

        def print_table(title, items):
            print(f"\n===== {title} =====")
            print(f"{'ID':<5} {'Item':<20} {'Half':<10} {'Full':<10}")
            print("-" * 50)

            for m in items:
                full = m["price"]
                half = full / 2
                print(f"{m['id']:<5} {m['name']:<20} ₹{half:<9} ₹{full:<9}")

        if veg:
            print_table(" VEG MENU", veg)

        if nonveg:
            print_table(" NON-VEG MENU", nonveg)

        if starter:
            print_table(" STARTERS", starter)

        if drinks:
            print_table(" SOFT DRINKS & DESSERTS ", drinks)


    
    def get_item_by_id(self, item_id):

        menu = Data.read(Data.MENU_PATH)

        for m in menu:
            if m["id"] == item_id:
                return m

        return None

