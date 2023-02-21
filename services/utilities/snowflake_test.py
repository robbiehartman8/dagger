
import re

name_list = ['robert', 'm', 'hartman', 'rob', 'm', 'hartman']

def cleanName(name_list):
    # change to have special characters later
    for index in range(len(name_list)):
        name = name_list[index].strip().lower()
        name = re.sub(r'[^a-zA-Z0-9]', '', name)
        name_list[index] = name

    return name_list[0:3], name_list[3:]

print(cleanName(name_list))



