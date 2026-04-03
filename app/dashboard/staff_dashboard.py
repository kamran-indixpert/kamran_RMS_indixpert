from app.menu.menu import Menu
from app.order.order import Order
from app.booking.booking import Booking
from app.billing.billing import Billing

class StaffDashboard:

    def menu(self):

        m = Menu()
        o = Order()
        b = Booking()
        c = Billing()

        while True:
            print("\n" + "="*35)
            print("       STAFF DASHBOARD")
            print("="*35)
            print("1. View Menu")
            print("2. Take Order")
            print("3. Book Table")
            print("4. Generate Bill")
            print("5. Logout")

            ch = input("Enter Your Choice: ").strip()

            try:
                if ch == "1":
                    m.view()

                elif ch == "2":
                    o.take_order()

                elif ch == "3":
                    b.book_table()

                elif ch == "4":
                    c.generate_bill()

                elif ch == "5":
                    print(" Logged out successfully")
                    break

                else:
                    print(" Invalid choice, try again")

            except Exception as e:
                print(" Something went wrong:", e)          

