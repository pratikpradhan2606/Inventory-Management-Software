import import_ipynb
import numpy as np
import datetime 
import matplotlib.pyplot as plt
from module1 import menu_card,check_exist,insert_entity,update_field_Name,is_empty,want_continue,update_field_Value,delete_field
print("~"*100)
print("\n                                   Inventory Management System                                 \n")
print("~"*100)
entity = {}
stock = {}
history_list=[]
e = datetime.datetime.now()
while(1):
    print("\nMenu:-             |-------------------------------------------------------|     Date:%s/%s/%s" % (e.day, e.month, e.year))
    print("                   |                    1.   Add Entity                    |     Time:%s:%s:%s" % (e.hour, e.minute, e.second))
    print("                   |-------------------------------------------------------|")
    print("                   |                    2.   Update Entity                 |")
    print("                   |-------------------------------------------------------|")
    print("                   |                    3.   Show Data                     |")
    print("                   |-------------------------------------------------------|")
    print("                   |                    4.   Delete Data                   |")
    print("                   |-------------------------------------------------------|")
    print("                   |                    5.   Request stock                 |")
    print("                   |-------------------------------------------------------|")
    print("                   |                    6.   Print History                 |")
    print("                   |-------------------------------------------------------|")
    print("\n")
    try:
        choice = int(input("Enter Your Choice \U0001f600: "))
    except:
        print("Operation Terminated!!!")
        break
    #choice 1 for Add entity field with quantity
    if choice == 1:
        print("\n\nSeems like you want to add Data!!\U0001f600 \U0001f600 ")
        field = input("\nEnter data Field : ")

        if check_exist(field,entity):#calling for verification of field exists or not
            print("\nThis Field Already Exists")
        else:
            try:
                quantity = int(input(f"How many items available for {field} :"))
                flag = insert_entity(entity, field, quantity)  # calling for data field insertion
                if flag:
                    print("-"*40)
                    print("|    Data Added Successfully\U0001f600\U0001f600   |")
                    print("-"*40)
                else:
                    print("-"*40)
                    print("|    Data Insertion Unsuccessfull!!!     |")
                    print("-"*40)

            except:
                print("\nOperation Terminated!!!")
            
                
    #choice2 for data updation
    elif choice==2:
        print("Seems like you want to Update Data!!")
        what_to_update = input("Enter What you want to update Field or Quantity")
        what_to_update.capitalize()
        if what_to_update.__eq__("Field"):
            print("                   |------------------- Available Fields -------------------|")
            for key,value in entity.items():
                print("                   |                       ",key,"                      |")
                print("                   |-------------------------------------------------------|")

            update_field=input("\nWhich field you want to update from above")
            update_field.title()

            if check_exist(update_field,entity):
                update_key = input("\nEnter new Name for Field : ")
                update_field_Name(update_field, entity, update_key)
                print("-"*40)
                print("|    Data Updated Successfully\U0001f600\U0001f600   |")
                print("-"*40)
            else:
                print("-"*40)
                print("|    Data Does Not Exists!!   |")
                print("-"*40)
        elif what_to_update.__eq__("Quantity"):
            print("                   |------------------- Available Fields -------------------|\n")
            for key, value in entity.items():
                print(f"                                    {key}   =>    {value}                   ")
                print("                   |-------------------------------------------------------  |")
                

            update_field = input("Which fields quantity you want to update from above")
            update_field.title()

            if check_exist(update_field, entity):
                try:
                    update_value = int(input("Enter Quantity : "))
                    update_field_Value(field, entity, update_value)
                    print("-"*40)
                    print("Field Quantity updated successfully")
                    print("-"*40)
                except:
                    print("\nOperation Terminated!!!")
            else:
                print("-"*40)
                print("Does not exists")
                print("-"*40)
        else:
            print("-"*40)
            print("Choice Not matching")
            print("-"*40)

    elif choice == 3:
        if is_empty(entity):
            print("No Data Available in Your Dashboard")
        else:
            print("Seems like you want to See the Data!!")
            print("So Your Current Data is")

            aplication=[]
            obj = []
            print("                   |------------------- Available Fields -------------------|\n")
            for key, value in entity.items():
                print(f"                                      {key}   =>    {value}                   ")
                print("                   |-------------------------------------------------------  |")
                obj.append(key)
                aplication.append(value)

            y_pos = np.arange(len(obj))
            plt.bar(y_pos,aplication,align='center',alpha=0.2)
            plt.xticks(y_pos,obj)
            plt.ylabel("Applications in X")
            plt.title("Inventory Management System")
            plt.show()

    elif choice == 4:
        print("Seems Like you want to delete Data")
        if is_empty(entity):
            print("but Dashboard is Empty Invalid Delete Operation")
        else:
            print("                   |------------------- Available Fields -------------------|\n")
            for key, value in entity.items():
                print(f"                                    {key}   =>    {value}                   ")
                print("                   |-------------------------------------------------------  |")
                

            del_field = input("Which field you want to Delete from above")
            if check_exist(del_field, entity):
                delete_field(del_field, entity)
                print("-"*40)
                print("Field Deleted successfully")
                print("-"*40)
            else:
                print("-"*40)
                print("Does not exists")
                print("-"*40)
    elif choice == 5:
        print("\nRequest Stock operation is turned on!!\n")
        if is_empty(entity):
            print("\nDashboard is Empty Cant do Request Operation\n")
        else:
            print("\n                   |------------------- Available Fields -------------------|\n")
            for key, value in entity.items():
                print(f"                                    {key}   =>    {value}                   ")
                print("                   |-------------------------------------------------------  |")
            person_name=input("Enter Person Name: ")
            item_want=input(f"Enter Which Item {person_name} want: ")
            if check_exist(item_want, entity):
                print("-"*40)
                print("\nRequested Item is Available")
                print("-"*40)
                item_quantity = int(input(f"How many Items {person_name} wants?"))
                if(item_quantity>0 and item_quantity<entity[item_want]):
                    entity[item_want]=entity[item_want]-item_quantity
                    print("-"*40)
                    print(f"Stock item issued to {person_name} for item quantity of {item_quantity} by Incharge")
                    print(f"Stock available for {item_want} is {entity[item_want]}")
                    history_list.append(f"\n {person_name}           {item_want}         {item_quantity}           {e.hour}:{ e.minute}:{ e.second}         {e.day}/{e.month}/{e.year}")
                    print("-"*40)
                else:
                    print("-"*40)
                    print("Operation Could Not be done")
                    print("-"*40)
            else:
                print("-"*40)
                print("Stock Not Available")
                print("-"*40)
    elif choice==6:
        f = open("StockHistory.txt","a")
        for l in history_list:
            f.write(l)
        f.close()
        print("Data is printed in StockHistory File")
    else:
        print("***************                     Select Valid Choice!!!                  **********************")

    if want_continue():
        print("Thanks for Confirmation")
    else:
        break
print("~"*100)
print("\n                          Thanks For Visiting Inventory System\U0001f600                                \n")
print("~"*100)        

