from session17 import Consultation
from session15 import Pet
from project2 import Customer
from project3 import DBHelper
from tabulate import tabulate

def consultation_menu():
    db = DBHelper()

    message = """
    >>CONSULTATION MENU<<
    1:Add Consultations
    2:Update Consultations
    3:View All Consultations
    4:View Consultations By Date
    5:View Customers Pets Consultation
    0: Quit
    """
    print(message)
    choice = int(input("Enter Your Choice:"))

    pet = Pet()
    customer = Customer()
    consultation = Consultation()
    while True:
        if choice == 1:
            phone = input("Enter Customer Phone:")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pets_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            if len(rows) == 0:
                print("Please Add Pet First")
                break
            if len(rows) == 1:
                pet.pid = rows[0][0]
            else:
                pet.pid = int(input("Enter Pet Id:"))

            consultation.cid = customer.cid
            consultation.pid = pet.pid
            consultation.read_consultation_data()
            print(vars(consultation))

            sql = consultation.get_insert_sql_query()
            db.execute_sql(sql)
            print("Consultation Added Successfully...")
        elif choice == 2:
            pass
        elif choice == 3:
            sql = consultation.get_consultation_sql_query()
            rows = db.execute_select_sql(sql)
            columns = ['CNID', 'CID', 'PID', 'PROBLEM', 'HEARTRATE', 'TEMP', 'MEDICINES', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
        elif choice == 4:
            pass
        elif choice == 5:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pets_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            pid = input("Enter Pet Id: ")

            sql = consultation.get_consultation_sql_query(pid=pid)
            rows = db.execute_select_sql(sql)
            columns = ['CNID', 'CID', 'PID', 'PROBLEM', 'HEARTRATE', 'TEMP', 'MEDICINES', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 0:
            break
        else:
            print("Invalid Choice")
        print(message)
        choice = int(input("Enter Your Choice:"))
