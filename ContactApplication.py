import time
data={1:{
        "f_name":"Aashish",
        "l_name":"Jangid",
        "phone_number":9571157004,
        "email_id":"aashishjangid9750@gmail.com"},
    2:{"f_name":"Sanju",
        "l_name":"Sharma",
        "phone_number":9856321452,
        "email_id":"sanju1652@gmail.com"},
    3:{"f_name":"Anu",
        "l_name":"Sharma",
        "phone_number":8548596023,
        "email_id":"anuavan786@gmail.com"}}
new=len(data)+1

def search_lname():
    lName=str(input("Enter the last name: ")).strip().title()
    msg="Finding"
    for i in range(10):
        msg=msg+"."
        print(f"{msg}\r",end="")
        time.sleep(.1)
    print("\n")
    for i in data:
        if data[i]["l_name"]==lName:
            print(f"""\tName:{data[i]["f_name"]} {data[i]["l_name"]}
        PhoneNo:{data[i]["phone_number"]}
        Email Id:{data[i]["email_id"]}\n""")
            search()
            return
    if data[i]["l_name"]!=lName:
        print("Not found")
        search()

def search_flname():
    FName=str(input("Enter the first name: ")).strip().title()
    LName=str(input("Enter the last name: ")).strip().title()
    msg="Finding"
    for i in range(10):
        msg=msg+"."
        print(f"{msg}\r",end="")
        time.sleep(.1)
    print("\n")
    for i in data:
        if data[i]["f_name"]==FName and data[i]["l_name"]==LName:
            print(f"""\tName:{data[i]["f_name"]} {data[i]["l_name"]}
        PhoneNo:{data[i]["phone_number"]}
        Email Id:{data[i]["email_id"]}\n""")
            search()
            return
    if data[i]["f_name"]!=FName and data[i]["l_name"]!=LName:
        print("Not found")
        search()

def add_contact():
    fname=input("Enter you first name: ").strip().title()
    lname=input("Enter you last name: ").strip().title()
    number=int(input("Enter you phone number: "))
    email=input("Enter you email address: ").strip().lower()
    data[new]={"f_name":fname,"l_name":lname,"phone_number":number,"email_id":email}
    msg="Saving your contact"
    for i in range(10):
        msg=msg+"."
        print(f"{msg}\r",end="")
        time.sleep(.1)
    print("\nContact saved")
    contact_menu()

def search():
    print("How you want to search ?\n1. Search by last name\n2. Search by first and last name\n3. Back")
    tinp=int(input("Your choice: "))
    if tinp==1:
        search_lname()
    elif tinp==2:
        search_flname()
    elif tinp==3:
        contact_menu()
    else:
        print('Invalid input try again')
        search()

def delete_contact():
    FName=str(input("Enter the first name: ")).strip().title()
    LName=str(input("Enter the last name: ")).strip().title()
    for i in data:
        if data[i]["f_name"]==FName and data[i]["l_name"]==LName:
            data.pop(i)
            msg="Deleting"
            for i in range(10):
                msg=msg+"."
                print(f"{msg}\r",end="")
                time.sleep(.1)
            print("\nDelete sucessfully")
            contact_menu()
            return
    if data[i]["f_name"]!=FName and data[i]["l_name"]!=LName:
        print("Not found")
        contact_menu()

def all_contact():
    msg="Finding all contact"
    for i in range(10):
        msg=msg+"."
        print(f"{msg}\r",end="")
        time.sleep(.1)
    print("\n")
    for i in data:
        print(f"""\tName:{data[i]["f_name"]} {data[i]["l_name"]}
        PhoneNo:{data[i]["phone_number"]}
        Email Id:{data[i]["email_id"]}\n""")
    contact_menu()

def contact_menu():
    print('''\tWelcome to yout contact application\n
    \t\t1. Add new contact
    \t\t2. Search contact
    \t\t3. Delete contact
    \t\t4. Show all contact
    \t\t5. Exit
    ''')
    user_input=int(input("Your choice:"))
    if user_input==1:
        add_contact()
    elif user_input==2:
        search()
    elif user_input==3:
        delete_contact()
    elif user_input==4:
        all_contact()
    elif user_input==5:
        print("\n\t\tThank you")
    else:
        print("Invalid input try again")
        contact_menu()
contact_menu()