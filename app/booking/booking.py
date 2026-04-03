from app.database.db import Data
import uuid

class Booking:

    FILE_PATH = Data.BOOKING_PATH   

    def book_table(self):

        bookings = Data.read(self.FILE_PATH) or []

        name = input("Enter Customer Name: ").strip()

        if not name:
            print(" Name cannot be empty")
            return

        try:
            table_count = int(input("How many tables you want to book: "))
        except ValueError:
            print(" Invalid number")
            return

        if table_count <= 0:
            print(" Enter valid table count")
            return

        booking = {
            "id": str(uuid.uuid4())[:6],
            "name": name,
            "tables": table_count,
            "status": "booked"
        }

        bookings.append(booking)

        Data.write(Data.BOOKING_PATH, bookings)

        print(" Tables booked successfully")

    def view_booking(self):

        bookings = Data.read(self.FILE_PATH) or []

        if not bookings:
            print(" No bookings found")
            return

        print("\n===== BOOKINGS =====")

        for b in bookings:
            print(f"{b['id']} | {b['name']} | Tables: {b['tables']} | {b['status']}")

    def cancel_booking(self):

        booking_id = input("Enter Booking ID: ").strip()

        bookings = Data.read(self.FILE_PATH) or []

        for b in bookings:
            if b["id"] == booking_id:
                bookings.remove(b)

                Data.write(Data.BOOKING_PATH, bookings)

                print(" Booking cancelled")
                return

        print(" Booking not found")




