from pprint import pprint
import csv
import re
from collections import defaultdict


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
               r'(\d{2})[-\s*]*(\d{2})\s*\(*(доб\.)*\s*(\d{4})*\)*')
    btf_number = r'+7(\2)\3-\4-\5 \6\7'
    for employee in my_list[1:]:
        new_phone = re.sub(pattern, btf_number, employee[-2])
        employee[-2] = new_phone
    return my_list

def delete_dupls(my_list):
    new_employees_dict = {}
    dupl_dict = {}
    for employee in my_list[1:]:
        new_employee = ' '.join(employee[0:2])
        if new_employee not in list(new_employees_dict.keys()):
            new_employees_dict[new_employee] = employee
        else:
            dupl_dict[new_employee] = employee
    dd = defaultdict(list)
    for key in set(list(new_employees_dict.keys()) + list(dupl_dict.keys())):
        if key in new_employees_dict:
            dd[key].append(new_employees_dict[key])
        if key in dupl_dict:
            dd[key].append(dupl_dict[key])
    dd = dict(dd)
    employee_list = list(dd.values())
    pprint(employee_list)

if __name__=='__main__':
    delete_dupls(new_phones(full_names(contacts_list)))

# with open("phonebook.csv", "w", encoding="utf-8") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
