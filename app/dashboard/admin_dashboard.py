from app.menu.menu import Menu
from app.reports.reports import Report


class AdminDashboard:

    def menu(self):

        m = Menu()
        r = Report()

        while True:
            print("\n===== ADMIN DASHBOARD =====")
            print("1. Add Menu")
            print("2. View Menu")
            print("3. Sales Report")
            print("4. Logout")

            ch = input("Enter choice: ").strip()

            if ch == "1":
                m.add()
            elif ch == "2":
                m.view()
            elif ch == "3":
                r.sales_report()
            elif ch == "4":
                break
            else:
                print(" Invalid choice")
