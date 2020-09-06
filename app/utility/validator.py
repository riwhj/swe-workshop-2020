def validate_name(name): 

    num=["0","1","2","3","4","5","6","7","8","9"]
    special=["!","@","#","%","$"]
    space =" "

    if name == "":
        return False

    for i in name:
        is_num= i in num
        is_special= i in special  
        is_space= i in space
        if is_num or is_special or is_space:
            return False
    return True

def validate_id(id):
    return True


def validate_phone_number(phone_number):
    return True
