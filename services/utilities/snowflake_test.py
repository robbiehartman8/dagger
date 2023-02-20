import re


legal_first_name = "robert"
legal_middle_name = "maurice"
legal_last_name = "hartman"

preferred_first_name = "rob"
preferred_middle_name = ""
preferred_last_name = "hartman"

def cleanName(first_name, middle_name, last_name):
    first_name = first_name.strip().lower()
    first_name = re.sub(r'[^a-zA-Z0-9]', '', first_name)
    middle_name = middle_name.strip().lower()
    middle_name = re.sub(r'[^a-zA-Z0-9]', '', middle_name)
    last_name = last_name.strip().lower()
    last_name = re.sub(r'[^a-zA-Z0-9]', '', last_name)

    return [first_name, middle_name, last_name]

def checkNameStatus(legal_name_list, preferred_name_list):
    name_status = False
    for i in zip(legal_name_list, preferred_name_list):
        if i[0] != i[1]:
            name_status = True
            break
    if name_status is True:
        return name_status, preferred_name_list
    else:
        return name_status, legal_name_list

legal_name_list = cleanName(legal_first_name, legal_middle_name, legal_last_name)
preferred_name_list = cleanName(preferred_first_name, preferred_middle_name, preferred_last_name)

# print(checkNameStatus([legal_first_name, legal_middle_name, legal_last_name], [preferred_first_name, preferred_middle_name, preferred_last_name]))
