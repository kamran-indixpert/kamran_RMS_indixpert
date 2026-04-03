from app.database.db import Data

class Report:

    def sales_report(self):

        orders = Data.read(Data.ORDER_PATH) or []

        if not orders:
            print(" No sales found")
            return

        total_sales = 0
        total_orders = len(orders)

        for o in orders:
            total_sales += o.get("total", 0)

        print("\n===== SALES REPORT =====")
        print(f"Total Orders : {total_orders}")
        print(f"Total Sales  : ₹{total_sales}")
        print("========================")

