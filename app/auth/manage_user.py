from app.auth.signup import Signup
from app.auth.login import Login
from app.log.logger import get_logger

class System:

    def start(self):

        while True:
            print('-'*30)
            print('RED HEAVEN RESTAURANT')
            print('-'*30)
            print("1 Signup\n2 Login\n3 Exit")
            ch = input("Please Enter Your Choice:")

            if ch == "1":
                Signup().register()
            elif ch == "2":
                Login().user_login()
            else:
                break


if __name__ == "__main__":
     System().start()