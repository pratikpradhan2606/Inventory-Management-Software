
y = ['Y','y','YES','yes','yES','yeS']
n = ['N','n','NO','no','No','nO']
def menu_card():
    pass

#check whether entity field already exists or not
def check_exist(field,entity):
    if (entity.get(field)):
        return True
    else:
        return False

#add data entry with quantity
def insert_entity(entity,field,quantity):
    if quantity>=0:
        entity[field]=quantity
        return True
    else:
        return False
    
def update_field_Name(field,entity,update_key):
    entity[update_key] = entity.pop(field)

def is_empty(entity):
    res = not entity
    return res

def want_continue():
    str = input("Do you want to continue Y/N")
    str.upper()
    if (str in n):
        return False
    elif (str in y):
        return True
    else:
        print("Please Select Valid Choice")
        want_continue()

def update_field_Value(field,entity,update_value):
    entity[field]=update_value


def delete_field(field,entity):
    del entity[field]