import json
import os

class Data:

    USER_PATH = "app/database/user.json"
    MENU_PATH = "app/database/menu.json"
    ORDER_PATH = "app/database/order.json"
    BOOKING_PATH = "app/database/booking.json"   

    @staticmethod
    def read(path):
        if not os.path.exists(path):
            return []
        try:
            with open(path, "r") as f:
                return json.load(f)
        except:
            return []

    @staticmethod
    def write(path, data):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def log(message):
        with open("log.txt", "a") as f:
            f.write(message + "\n")

