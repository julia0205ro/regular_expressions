from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

def full_names(my_list):
    new_employee_list = []
    for full_name in my_list[1:]:
        employee_full_name = ' '.join(full_name[:3])
        employee_full_name_list = employee_full_name.split()
        full_name = full_name[3:]
        new_employee = employee_full_name_list + full_name
        new_employee_list.append(new_employee)
    new_contacts_list = my_list[:1] + new_employee_list
    return new_contacts_list

def new_phones(my_list):
    pattern = (r'(8|\+7)\s*\(*(\d{3})\)*[-\s*]*(\d{3})[-\s*]*'
               r'(\d{2})[-\s*]*(\d{2})\s*\(*(доб\.)*\s*(\d{4})*')
    btf_number = r'+7(\2)\3-\4-\5 \6\7'
    for employee in my_list[1:]:
        for data in employee:
            new_phone = re.sub(pattern, btf_number, data)
            print(new_phone)


pprint(new_phones(full_names(contacts_list)))

# with open("phonebook.csv", "w", encoding="utf-8") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
