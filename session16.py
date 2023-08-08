from session16A import consultation_menu
from session16B import pets_menu
from session16C import customer_menu
import datetime

def main_menu():

    message = """
    >>MAIN MENU<<
    1: Manage Customers
    2: Manage Pets
    3: Manage Consultations
    0: Quit
    """
    print(message)
    choice = int(input("Enter Your Choice:"))
    while True:
        if choice == 1:
            customer_menu()
        elif choice == 2:
            pets_menu()
        elif choice == 3:
            consultation_menu()
        elif choice == 0:
            break
        else:
            print("Invalid Choice")

        print(message)
        choice = int(input("Enter Your Choice:"))

def main():
    date1 = datetime.datetime.today()
    welcome = """
    ~~~~~~~~~~~~~~~
    Welcome To Vets App
    ~~~~~~~~~~~~~~~~
    """
    print(welcome)
    main_menu()
    bye_message = """
    ~~~~~~~~~~~~~~~~
    Thankyou For Using Vets App
    """
    print(bye_message)
    date2 = datetime.datetime.today()
    print("App usage:", date1 - date2)
if __name__ == "__main__":
    main()