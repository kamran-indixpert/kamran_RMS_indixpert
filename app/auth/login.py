from app.database.db import Data
from app.dashboard.admin_dashboard import AdminDashboard
from app.dashboard.staff_dashboard import StaffDashboard
import getpass

class Login:

    def user_login(self):

        users = Data.read(Data.USER_PATH)

        
        while True:
            email = input("Enter Email: ").strip()

            if not email:
                print(" Email required")
                continue
        
            if email.count("@") != 1:
                print(" Email must contain exactly one '@'")
                continue

            username, domain = email.split("@")

            if not username or not domain or "." not in domain:
                print(" Invalid email format")
                continue

            break

    
        password = getpass.getpass("Enter Password: ")

        found = False

        for user in users:

            if user["email"] == email:
                found = True

                
                if user.get("status") != "active":
                    print(" Account blocked")
                    return

                
                if user["password"] != password:
                    print(" Wrong password")
                    return

                print(" Login Successful")

                
                if user["role"] == "admin":
                    AdminDashboard().menu()
                else:
                    StaffDashboard().menu()

                return

        if not found:
            print(" User not found")


