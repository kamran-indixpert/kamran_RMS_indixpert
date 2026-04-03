from app.database.db import Data
import uuid
import getpass
import re

class Signup:

    def generate_id(self):
        return str(uuid.uuid4())[:8]

    def register(self):

        users = Data.read(Data.USER_PATH) or []

        
        while True:
            name = input("Enter Name: ").strip()

            if not name:
                print(" Name required")
                continue

            if not re.fullmatch(r"[A-Za-z ]+", name):
                print(" Name should contain only letters")
                continue

            break

        
        while True:
            email = input("Enter Email: ").strip()

            if email.count("@") != 1:
                print(" Email must contain exactly one '@'")
                continue

            username, domain = email.split("@")

            if not username or not domain or "." not in domain:
                print(" Invalid email format")
                continue

            if any(u.get("email") == email for u in users):
                print(" Email already registered")
                continue

            break

        
        while True:
            password = getpass.getpass("Enter Password: ")

            if len(password) < 6:
                print(" Password must be at least 6 characters")
                continue

            if not any(c.isupper() for c in password):
                print(" Must contain 1 uppercase letter")
                continue

            if not any(c.islower() for c in password):
                print(" Must contain 1 lowercase letter")
                continue

            if not any(c.isdigit() for c in password):
                print(" Must contain 1 number")
                continue

            confirm = getpass.getpass("Confirm Password: ")

            if password != confirm:
                print(" Passwords do not match")
                continue

            break

        
        user = {
            "id": self.generate_id(),
            "name": name,
            "email": email,
            "password": password,   
            "role": "staff",
            "status": "active"
        }

        users.append(user)

        Data.write(Data.USER_PATH, users)

        print(" Signup Successfully")

