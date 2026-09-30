import sys
import os

# fix paths
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.user_management import *
from modules.train_management import *
from modules.booking import *
from utils.ui import *
from utils.validation import *

def main():
    # init stuff
    um=UserManagement()
    tm= TrainManagement()
    bm =BookingSystem(tm)
    
    currentUser = None

    while True:
        if currentUser==None:
            print_header("MET-RO: Metro Train Reservation System")
            print_menu(["Login", "Register"])
            c = get_int_input("Choose an option: ",0,2)

            if c == 0:
                print("Thank you for using MET-RO. Goodbye!")
                break
            elif c ==1:
                print_header("Login")
                usr = input("Enter Username: ")
                pwd = input("Enter Password: ")
                userData=um.login(usr, pwd)
                if userData:
                    currentUser = {"username":usr, **userData}
                pause()
            elif c== 2:
                print_header("Register")
                usr = input("Choose a Username: ")
                pwd = input("Choose a Password (min 4 chars): ")
                um.register(usr,pwd)
                pause()
        
        else:
            # user dash
            print_header("MET-RO Dashboard - Hello, %s!" % currentUser['username'])
            opts=[
                "View Available Trains",
                "Book a Ticket",
                "View My Bookings",
                "Cancel a Ticket",
                "Logout"
            ]
            print_menu(opts)
            c = get_int_input("Choose an option: ", 0,5)

            if c == 0:
                print("Thank you for using MET-RO. Goodbye!")
                break
            elif c== 1:
                print_header("Available Trains")
                tm.display_trains()
                pause()
            elif c== 2:
                print_header("Book a Ticket")
                tm.display_trains()
                t_id=input("Enter Train ID to book: ").strip().upper()
                if tm.get_train(t_id):
                    num_tks = get_int_input("Number of tickets: ",1, 10)
                    bm.book_ticket(currentUser['username'],t_id, num_tks)
                else:
                    print_error("Invalid Train ID.")
                pause()
            elif c ==3:
                print_header("My Bookings")
                bm.view_my_bookings(currentUser['username'])
                pause()
            elif c == 4:
                print_header("Cancel a Ticket")
                bm.view_my_bookings(currentUser['username'])
                tktId = input("Enter Ticket ID to cancel: ").strip().upper()
                bm.cancel_ticket(currentUser['username'], tktId)
                pause()
            elif c== 5:
                currentUser=None
                print_success("Logged out successfully.")
                pause()

if __name__ == "__main__":
    # make sure dir exists
    if not os.path.exists("data"): os.makedirs("data")
    main()
