from app.database.db import Data

class Billing:

    def generate_bill(self):

        orders = Data.read(Data.ORDER_PATH) or []

        total = sum(o.get("total", 0) for o in orders)

        gst = total * 0.05
        final = total + gst

        print("\n===== BILL =====")
        print(f"Subtotal: ₹{total}")
        print(f"GST: ₹{gst}")
        print(f"Final: ₹{final}")